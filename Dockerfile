FROM python:3.7.2-alpine3.9 

COPY requirements.txt ./

RUN alias python=python3
RUN alias pip=pip3

RUN apk add --no-cache \
  postgresql \
  python3-dev \
  postgresql-dev \
  build-base

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app/

EXPOSE 8080

CMD ["python", "manage.py", "run_server"]