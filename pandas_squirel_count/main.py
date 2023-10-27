import pandas as pd


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231027.csv")
data['Primary Fur Color'].value_counts().to_csv("liczba_wiewiorek.csv")
