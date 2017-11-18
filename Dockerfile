FROM python:2
MAINTAINER Florin Stancu (stancu.florin23@gmail.com)

ADD requirements.txt /
COPY *.py /
COPY config/*.ini /config/

RUN pip install -r requirements.txt
CMD ["python", "./artik_cloud.py"]