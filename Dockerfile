# Pull official base Python Docker image
FROM python:3.11.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /techietoxpress

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /techietoxpress/
RUN pip install -r requirements.txt

# Copy the Django project
COPY . /techietoxpress/
