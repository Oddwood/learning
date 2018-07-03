FROM python:3

COPY ./code /app
WORKDIR /app
RUN pip install -r requirements.txt && FLASK_APP=app.py

CMD [ "flask", "run", "--host=0.0.0.0" ]

EXPOSE 5000