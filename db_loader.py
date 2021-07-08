from boto3.dynamodb.conditions import Key, Attr
import boto3
import os


def test(parameter):
    return (
        os.environ["AWS_ACCESS_KEY_ID"],
        os.environ["AWS_SECRET_ACCESS_KEY"],
        os.environ["AWS_SESSION_TOKEN"],
    )
