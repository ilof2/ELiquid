FROM python:3.8.5 as builder

RUN apt-get update \
   && apt-get install -y libpng-dev libpq-dev git python-dev python3-dev \
   && apt-get install -y g++ make wget less ca-certificates openssl \
   && pip install --no-cache-dir --upgrade pip \
   && pip install --no-cache-dir pipenv

ENV PYTHONUNBUFFERED 1
ENV LIBRARY_PATH=/lib:/usr/lib
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system

FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV LIBRARY_PATH=/lib:/usr/lib
ENV APP_HOST=0.0.0.0
ENV APP_PORT=5000
EXPOSE ${APP_PORT}

COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY ./src /opt/app
COPY /Pipfile /opt/app


WORKDIR /opt/app

RUN mkdir -p /opt/app/data

VOLUME ["/opt/app/data"]
RUN pip3 install python-dotenv
CMD ["python3", "app.py"]
