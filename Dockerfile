#Deriving the latest base image
FROM python:latest

LABEL Maintainer="GaussDev"

WORKDIR /usr/app/src

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "python", "./bot.py"]