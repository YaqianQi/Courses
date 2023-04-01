FROM ubuntu:bionic

ENV ROOT_PATH="/opt/my_service"

ADD requirements.txt requirements.txt
RUN echo installing \
    && apt-get update -qq \
    && apt-get install -y \
        python3 \
        python3-pip \
    && pip3 install -r requirements.txt \
    && mkdir -p ${ROOT_PATH}

COPY app.py ${ROOT_PATH}
WORKDIR ${ROOT_PATH}

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
