FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="techietoxpress.com"

COPY ./proxy/default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./proxy/uwsgi_params /etc/nginx/uwsgi_params
COPY ./scripts /scripts
COPY ./scripts/run.sh /run.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=techietoxpress
ENV APP_PORT=9000

USER root


RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
        /venv/bin/pip install -r /requirements.txt && \
        apk del .tmp-deps && \
        adduser --disabled-password --no-create-home techietoxpress && \
        mkdir -p /vol/web/static && \
        mkdir -p /vol/web/media && \
        chown -R techietoxpress:techietoxpress /vol && \
        chmod -R 755 /vol && \
        chmod -R +x /scripts


ENV PATH="/scripts:/venv/bin:$PATH"

USER techietoxpress

CMD ["/run.sh"]


