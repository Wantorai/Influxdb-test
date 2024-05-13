from influxdb_client import InfluxDBClient, Point
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


# Параметры подключения к базе данных
url = 'http://iot.mmr.systems:8086/'
token = 'wxoi_yuT-G2GfujTM1QiyLbXic9ezxr9N_iL-NzM0f42uZwBn6tXQJZI3TvBjBq6r810vxkB9-xFFG2FQAUWsQ=='
org = 'mmr.systems'
bucket = 'test-bucket'
field = 'i1'
measurement = 'Irms'

# Подключаемся к базе данных InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)


# Запрос данных из базы данных InfluxDB
query = f'from(bucket:"{bucket}") |> range(start: -6h) |> filter(fn: (r) => r._measurement == "{
    measurement}") |> filter(fn: (r) => r._field == "{field}")'


result = client.query_api().query_data_frame(query)

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(result.index, result['_value'], marker='o', linestyle='-')
plt.title(f'График данных из InfluxDB ({measurement}.{field})')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.show()
