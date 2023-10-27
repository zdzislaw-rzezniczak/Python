# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != ("temp"):
#             temperature.append(row[1])
#
# print(temperature)

import pandas as pd


data = pd.read_csv("weather_data.csv")
# temp_list = data['temp'].to_list()
#
# print(temp_list)
# max = data['temp'].max()
# print(max)

monday = data[data.day == "Monday"]
print(monday.temp * 9 / 5 + 32)
# print(data[data.temp == data.temp.max()])