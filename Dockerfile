FROM python

WORKDIR /code

COPY ./requerements.txt /code/

RUN pip install -r requerements.txt

COPY . .