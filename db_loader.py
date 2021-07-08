from boto3.dynamodb.conditions import Key, Attr
from botocore.config import Config
import boto3

DB_TABLE = "wunderground_pws"


aws_config = Config(
    region_name="us-east-1",
    signature_version="v4",
    retries={"max_attempts": 10, "mode": "standard"},
)


def db_load() -> list:
    dynamodb = boto3.resource("dynamodb", config=aws_config)
    table = dynamodb.Table(DB_TABLE)

    response = table.scan()
    items = response["Items"]

    # LastEvaluatedKey indicates that there are more results
    while "LastEvaluatedKey" in response:
        response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        items.extend(response["Items"])

    return items
