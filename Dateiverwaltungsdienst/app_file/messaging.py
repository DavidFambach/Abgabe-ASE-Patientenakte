import logging
import pika
import time
import threading

from django.conf import settings
from typing import Callable, Union

DELETE_USER_CALLBACK: Union[Callable[[int], None], None] = None


class _Parameters:
    queue_host: str
    queue_port: int
    queue_username: str
    queue_password: str
    queue_exchange_name: str
    def __init__(self, queue_host: str, queue_port: int, queue_username: str, queue_password: str, queue_exchange_name: str):
        self.queue_host = queue_host
        self.queue_port = queue_port
        self.queue_username = queue_username
        self.queue_password = queue_password
        self.queue_exchange_name = queue_exchange_name

class _UserUpdateDaemon(threading.Thread):

    active: bool
    active_lock: threading.Lock
    queue_parameters: _Parameters

    def __init__(self, queue_parameters: _Parameters):
        super().__init__()
        self.daemon = True

        self.active = True
        self.active_lock = threading.Lock()
        self.queue_parameters = queue_parameters
        self.channel = None

    def run(self) -> None:
        credentials = pika.PlainCredentials(username=self.queue_parameters.queue_username, password=self.queue_parameters.queue_password)
        connection_parameters = pika.ConnectionParameters(host=self.queue_parameters.queue_host, port=self.queue_parameters.queue_port, credentials=credentials)
        while self.active:
            try:

                connection = pika.BlockingConnection(connection_parameters)
                channel = connection.channel()
                with self.active_lock:
                    if not self.active:
                        return
                    self.channel = channel
                channel.exchange_declare(exchange=self.queue_parameters.queue_exchange_name, exchange_type="fanout")
                result = channel.queue_declare(queue="", exclusive=True)
                queue_name = result.method.queue
                channel.queue_bind(exchange=self.queue_parameters.queue_exchange_name, queue=queue_name)

                channel.basic_consume(queue=queue_name, on_message_callback=_handle_message, auto_ack=True)
                channel.start_consuming()

            except Exception as e:
                logging.warning("Encountered an exception when running the message listener")
                logging.exception(e)
                time.sleep(1)

    def stop(self):
        with self.active_lock:
            self.active = False
            channel = self.channel
            if channel is not None:
                channel.stop_consuming()

_current_listener: Union[_UserUpdateDaemon, None] = None

def start_listener():
    global _current_listener
    if _current_listener is not None:
        raise RuntimeError("listener is already active")
    logging.info("Starting user deletion listener")
    queue_settings = settings.MESSAGE_QUEUES["user_update"]
    try:
        p = _Parameters(queue_host=queue_settings["host"], queue_port=int(queue_settings["port"]), queue_username=queue_settings["username"], queue_password=queue_settings["password"], queue_exchange_name=queue_settings["exchange_name"])
    except ValueError as e:
        raise RuntimeError("Bad user queue configuration: " + str(e))
    _current_listener = _UserUpdateDaemon(p)
    _current_listener.start()

def stop_listener():
    global _current_listener
    if _current_listener is None:
        raise RuntimeError("listener is not active")
    logging.info("Stopping user deletion listener")
    _current_listener.stop()
    _current_listener.join()
    _current_listener = None

def _handle_message(_channel, _method, _properties, body):
    try:
        if len(body) != 8:
            raise ValueError("Expected 8 bytes, got %s" % len(body))
        deleted_user_id = int.from_bytes(body, byteorder="big")
    except ValueError:
        logging.info("Encountered an invalid deleted user id. Ignoring that message")
        return
    _delete_user(deleted_user_id)

def _delete_user(user_id: int) -> None:
    logging.info("Received message that the user with ID %s has been deleted" % user_id)
    if DELETE_USER_CALLBACK is None:
        logging.info("No delete user callback is defined. Ignoring that message")
        return
    try:
        DELETE_USER_CALLBACK(user_id)
    except Exception as e:
        logging.info("Failed to delete user with ID %")
        logging.exception(e)