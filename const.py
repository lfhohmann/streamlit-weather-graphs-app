DB_TABLE = "wunderground_pws_short"

PARAMETERS_MAP = {
    "Temperature": "temp",
    "Temperature Feeling": "temp_feel",
    "Dew Point": "dew_point",
    "Humidity": "humidity",
    "Pressure": "pressure",
    "Wind Speed": "wind_speed",
    "Wind Gust": "wind_gust",
    "Wind Direction": "wind_direction",
    "Wind Bearing": "wind_bearing",
    "Precipitation Rate": "precip_rate",
    "Precipitation Total": "precip_total",
    "UV Index": "uv_index",
    "Solar Radiation": "radiation",
    "Last Updated": "last_updated",
}

UNITS_SCALE_FACTORS = {
    "station_id": 0,
    "last_updated": 0,
    "timestamp": 0,
    "temp": 10,
    "temp_feel": 10,
    "dew_point": 10,
    "humidity": 0,
    "pressure": 100,
    "wind_speed": 10,
    "wind_gust": 10,
    "wind_direction": 0,
    "wind_bearing": 0,
    "precip_rate": 100,
    "precip_total": 100,
    "uv_index": 0,
    "radiation": 10,
}
