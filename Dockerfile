FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 7373

CMD [ "python", "main.py" ]