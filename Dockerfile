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

WORKDIR /techietoxpress

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /requirements.txt

ENV PATH ="/venv/bin:$PATH"

USER techietoxpress

