#Set base image
FROM python:3.8

WORKDIR /src

ENV DB_NAME=database
    DB_USERNAME=DatabaseManager
    PASSWORD=A4NSd8qpHx8WfyNN

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

CMD ["python", "./main.py"]