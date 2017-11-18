FROM python:latest
MAINTAINER Florin Stancu (stancu.florin23@gmail.com)

ADD requirements.txt /
ADD artik_cloud.py /
ADD samsung_smart_tv_remote.py /

RUN pip install -r requirements.txt
CMD ["python", "./artik_cloud.py"]