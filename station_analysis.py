import pandas as pd
from glob import glob

filelist = glob('dataset/weather_*.csv')
valid_regions = [
    "S",
    "SE",
]

stations = pd.read_csv('dataset/stations.csv')
filtered_stations = stations[stations.region.isin(valid_regions)]


print()