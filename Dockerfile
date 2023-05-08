FROM python:3.11.3-alpine3.17

LABEL maintainer="techietoxpress.com"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set work directory
# Install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
COPY ./techietoxpress /techietoxpress
COPY ./scripts /scripts

WORKDIR /techietoxpress

EXPOSE 8000

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

CMD ['run.sh']