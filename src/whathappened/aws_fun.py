"""
Handle communcation with AWS.
"""

import boto3


def sync_bucket(bucket_name):
    s3_objects = list_bucket_objects(bucket_name)
    for s3_object in s3_objects:
        download_s3_object(bucket_name, s3_object)


def list_bucket_objects(bucket_name):
    s3 = boto3.client("s3")
    objects = s3.list_objects_v2(Bucket=bucket_name)["Contents"]
    return objects


def download_s3_object(bucket_name, s3_object):
    s3 = boto3.client("s3")
    object_name = s3_object["Key"]
    s3.download_file(bucket_name, object_name, object_name)
