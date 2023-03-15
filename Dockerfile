FROM python:3.9
RUN apt-get update && apt-get install -y net-tools nodejs npm

WORKDIR /app

ENV FLASK_APP=motopp
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV ENV=prod

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . ./motopp
CMD ["flask", "run"]