FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app-proyecto
WORKDIR /app-proyecto
COPY . /app-proyecto/
RUN pip install -r requirements.txt