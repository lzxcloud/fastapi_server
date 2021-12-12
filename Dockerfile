FROM python:3.8.0

RUN mkdir /code \
&&apt-get update \
&&apt-get -y install freetds-dev \
&&apt-get -y install unixodbc-dev

COPY requirements.txt /code
COPY /app /code

WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]