FROM python:3.9

RUN mkdir "motopp"

RUN apt-get update && apt-get install -y net-tools
RUN pip install mysql-connector-python

COPY . ./motopp

RUN pip install -r motopp/requirements.txt
RUN mv motopp/ENV motopp/.env

ENV ENV=prod
EXPOSE 5000