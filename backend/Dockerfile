# set base image (host OS)
FROM python:3.9.7

WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

