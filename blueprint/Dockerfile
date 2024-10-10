FROM python:3.11

WORKDIR /flaskpractice/blueprint

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
WORKDIR /flaskpractice/blueprint/blueprintapp

RUN python -m flask db init
RUN python -m flask db migrate
RUN python -m flask db upgrade

WORKDIR /flaskpractice/blueprint

CMD ["python","run.py"]