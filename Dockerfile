FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app-proyecto
WORKDIR /app-proyecto
COPY . /app-proyecto/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install nano
RUN cat ./replace.txt >> /usr/local/lib/python3.8/site-packages/flask_appbuilder/views.py