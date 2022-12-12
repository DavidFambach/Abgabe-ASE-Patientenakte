# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./AuthService /code/AuthService
COPY ./authentication /code/authentication
COPY ./social_auth /code/social_auth
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
	&& apt-get autopurge \
	&& rm -rf /var/lib/apt/lists/*
COPY ./config/nginx-proxy.conf /etc/nginx/sites-enabled/proxy-redirect.conf
# Need privileged execution to allow starting the nginx service. To reduce privileges of the Django server, the starup script needs to drop privileges selectively.
CMD ["python", "./run.py"]
