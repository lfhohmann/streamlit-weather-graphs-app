# from boto3.dynamodb.conditions import Key, Attr
import pandas as pd
import boto3

from const import *

def _convert_units(items_in) -> list:
    items_out = []

    for item_in in items_in:
        item_out = {}

        for key in UNITS_SCALE_FACTORS:
            if key in item_in:
                if type(item_in[key]) == str:
                    item_out[key] = item_in[key]
                else:
                    if UNITS_SCALE_FACTORS[key] == 0:
                        item_out[key] = int(item_in[key])
                    else:
                        item_out[key] = int(item_in[key]) / UNITS_SCALE_FACTORS[key]
            else:
                item_out[key] = None

        items_out.append(item_out)

    return items_out


def _db_load() -> list:
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(DB_TABLE)

    response = table.scan()
    items = response["Items"]

    # LastEvaluatedKey indicates that there are more results
    while "LastEvaluatedKey" in response:
        response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        items.extend(response["Items"])

    return items


def load_data() -> pd.DataFrame:
    items = _db_load()
    items = _convert_units(items)

    return pd.DataFrame(items)


if __name__ == "__main__":
    df = load_data()
    print(df[["station_id", "temp", "pressure"]])
