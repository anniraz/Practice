FROM python:3.8

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get install netcat -y

RUN apt-get upgrade -y && apt-get install -y  postgresql gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "/app/entrypoint.sh" ]

# 



# FROM python:3.8

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /code

# COPY requirements.txt /code

# RUN pip install -r /code/requirements.txt

# COPY . /code

# EXPOSE 8000

