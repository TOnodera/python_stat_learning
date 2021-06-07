FROM python:3.6.13-buster

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3-tk xterm
RUN pip install jupyter==1.0.0 ipython==6.2.1 notebook==5.0.0 numpy==1.14.3 pandas==0.23.0 matplotlib==2.2.2 statsmodels==0.9.0
RUN pip install flake8 && pip install autopep8

WORKDIR /home/python/app
RUN useradd -u 1000 -om python && \
    chown -R python:python /home/python