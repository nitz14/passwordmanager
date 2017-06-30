FROM alpine:latest

RUN apk add --update python3 python3-dev py-pip bash postgresql-dev gcc musl-dev libffi-dev make yarn &&\
  python3 -m ensurepip &&\
  rm -r /usr/lib/python*/ensurepip && \
  pip3 install --upgrade pip setuptools && \
  if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
  rm -r /root/.cache

ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install -qr /tmp/requirements.txt

ADD . /opt/passwordmanager
WORKDIR /opt/passwordmanager
RUN adduser -D passwordmanager &&\
  chown -R passwordmanager /opt/passwordmanager

USER passwordmanager

RUN cd /opt/passwordmanager &&\
  yarn install 

CMD gunicorn --bind 0.0.0.0:$PORT password_manager.wsgi
