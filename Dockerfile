ARG BASE_DOCKER=nvidia/cuda:10.1-base-ubuntu18.04
FROM $BASE_DOCKER

LABEL maintainer="diede@didirus.com"

ARG DEBIAN_FRONTEND=noninteractive

## Install OS requirements ##
RUN apt-get update --fix-missing \
 && apt-get dist-upgrade -y \
 && apt-get install -y --no-install-recommends python3-easygui \
      git vim build-essential less \
      nano \
      curl \
      ca-certificates \
      python3 \
      python3-distutils \
      python3-opencv \
      python3-dev \
      g++ \
      libpython3.6 \
      libxml2 \
      libxslt1.1 \
      libopenblas-base \
      libmagick++-6.q16-7 \
      libopencv-flann3.2 \
      libopencv-imgcodecs3.2 \
      libopencv-imgproc3.2 \
      libopencv-core3.2 \
      libgdal20 \
      locales ruby-dev \
 && apt-get autoremove -y \
 && apt-get purge -y $(dpkg -l | awk '{if($1=="rc")print $2}') \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py \
 && python3 /tmp/get-pip.py --no-wheel
RUN locale-gen \
 en_US.UTF-8 \
 de_DE.utf8

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt; rm requirements.txt

COPY entrypoint.sh /opt/didirus/
RUN chmod g+x /opt/didirus/entrypoint.sh

COPY tessa /opt/didirus/tessa

ENV PYTHONPATH /opt/didirus/

RUN useradd -m -u 1085 appuser
RUN chown -R appuser /opt/didirus

USER 1085
WORKDIR /opt/didirus

RUN chmod 700 /opt/didirus/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
