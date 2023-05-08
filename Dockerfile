FROM python:3.11-alpine3.17
LABEL maintainer="techietoxpress.com"

ENV PYTHONNUNBUFFERED 1

COPY requirements.txt /requirements.txt

RUN apk add --upgrade --no-cache build-base linux-headers && \
pip install --upgrade pip && \
pip install -r /requirements.txt

COPY techietoxpress/ /techietoxpress
WORKDIR /techietoxpress

RUN adduser --disabled-password --no-create-home techietoxpressadminuser
USER techietoxpressadminuser

CMD ["uwsgi","--socket",":9000","--workers","4","--master","--enabled-threads","--module","techietoxpress.wsgi"]