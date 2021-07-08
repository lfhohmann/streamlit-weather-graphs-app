from boto3.dynamodb.conditions import Key, Attr
import boto3

DB_TABLE = "wunderground_pws"


def db_load() -> list:
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(DB_TABLE)

    response = table.scan()
    items = response["Items"]

    # LastEvaluatedKey indicates that there are more results
    while "LastEvaluatedKey" in response:
        response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        items.extend(response["Items"])

    return items
