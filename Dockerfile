### 1. Get Linux
FROM python:alpine3.12

ENV JAVA_HOME="/usr/lib/jvm/default-jvm/"

RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    bash \
    curl \
    musl-dev \
    openjdk11 \
    postgresql-dev \
    postgresql-libs \
    gcc \
    libc-dev \
    python3-dev \
    && pip install psycopg2

ENV PATH=$PATH:${JAVA_HOME}/bin
ADD . .
RUN pip install -r requirements.txt
CMD ["./demo.sh"]
