FROM python:3.6

WORKDIR /store-manager-flask

COPY requirements.txt /store-manager-flask

RUN pip install -r requirements.txt

COPY . /store-manager-flask

CMD ["python", "manage.py", "runserver"]