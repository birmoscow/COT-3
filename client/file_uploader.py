# file_uploader.py MinIO Python SDK example
from minio import Minio
from minio.error import S3Error
import os
from time import sleep
import sys

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    print("PYTHON: py is ready, 5 sec", file=sys.stderr)
    sleep(5)
    client = Minio("host.docker.internal:9000",
        access_key="rfl4T2mzpfoz58xPzzuz",
        secret_key="1FgHHKhCPXU8si4pA4WkY91wEtLJsTxptosrrwNe",
        secure=False,
    )

    # The file to upload, change this path if needed
    source_file = ""

    # The destination bucket and filename on the MinIO server
    bucket_name = "test"
    destination_file = "photo.jpg"
    
    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        print("No bucket", bucket_name)
        exit(1)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    for f in os.listdir("/Meme pack by LiquidIllusion"):
        source_file = '/Meme pack by LiquidIllusion'
        print(f)
        client.fput_object(
            bucket_name, f, source_file + '/' + f,
        )
        print(
            source_file, "successfully uploaded as object",
            destination_file, "to bucket", bucket_name,
        )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)