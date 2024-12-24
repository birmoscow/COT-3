FROM python:3

WORKDIR /

RUN pip install minio

COPY . .

CMD [ "python", "./file_uploader.py" ]