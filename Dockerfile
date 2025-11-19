FROM python:3-alpine

WORKDIR /app

COPY requirements.txt /app/
COPY templates/* /app/templates/

COPY *.py /app/

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]