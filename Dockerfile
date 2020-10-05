FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /django_tutorial
ADD requirements.txt /django_tutorial/
RUN pip install -r requirements.txt
ADD . /django_tutorial/
