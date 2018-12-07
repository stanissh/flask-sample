FROM python:3.6-alpine
ADD . /app
WORKDIR /app
RUN pip install .
RUN python setup.py install
EXPOSE 5050