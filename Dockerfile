# Dockerfile

# Pull base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /techietoxpress

# Install dependencies
COPY requirements.txt /techietoxpress/
RUN pip install -r requirements.txt

# Copy project
COPY . /techietoxpress/

