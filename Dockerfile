FROM python:3.10

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip cmake wget llvm

WORKDIR /lemmecook_backend

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt --verbose

RUN pip install -U django-jazzmin

RUN pip install python-dotenv supabase psycopg2-binary django-cors-headers geopy redis

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 192.168.110.233:8000"]