FROM python:3

COPY ./code /www
WORKDIR /www
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=development

# host 0: is required in order to listen on incoming requests
CMD flask run --host=0.0.0.0 