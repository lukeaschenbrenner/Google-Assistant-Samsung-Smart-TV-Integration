FROM python:latest
MAINTAINER Florin Stancu (stancu.florin23@gmail.com)

RUN pip install -r requirements.txt
CMD ["python", "./artik_cloud.py"]