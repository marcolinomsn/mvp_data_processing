import pandas as pd
from glob import glob

filelist = glob('dataset/weather_*.csv')
valid_regions = [
    "S",
    "SE",
]

stations = pd.read_csv('dataset/stations.csv')
filtered_stations = stations[stations.region.isin(valid_regions)]

for filename in filelist:
    data = pd.read_csv(filename)
    data = data[data.ESTACAO.isin(filtered_stations.id_station)]
    output_filename = filename.replace('dataset', 'dataset_filtered')
    data.to_csv(output_filename, index=False)
    print()
