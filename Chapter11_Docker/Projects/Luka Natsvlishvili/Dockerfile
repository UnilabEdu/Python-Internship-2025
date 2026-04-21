FROM python:3.12-slim-bookworm

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y gcc build-essential python3-dev
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["uwsgi", "uwsgi.ini"]