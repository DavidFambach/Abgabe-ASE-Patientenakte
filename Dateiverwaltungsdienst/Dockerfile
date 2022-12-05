# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./fileservice /code/fileservice
COPY ./app_file /code/app_file
COPY ./manage.py ./requirements.txt ./run.py /code/
RUN pip install -r requirements.txt
RUN set -x \
    && addgroup --system --gid 105 nginx \
    && adduser --system --disabled-login --ingroup nginx --no-create-home --home /nonexistent --gecos "nginx user" --shell /bin/false --uid 105 nginx \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests --yes nginx \
	&& ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && rm /etc/nginx/sites-enabled/default \
	&& apt-get autopurge
COPY ./config/nginx-proxy.conf /etc/nginx/sites-enabled/proxy-redirect.conf
CMD ["python", "./run.py"]
