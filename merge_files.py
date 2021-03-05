# !/usr/bin/python3

import os
import pandas as pd

import json
import csv

root = '/media/data/shared/adsb'
 
class DataWriter():
    def __init__(self):
        self.output_filepath = None
        self.file = None

    def open_hourly_file(self, filepath):
        self.file = open(filepath, 'a') 
        self.writer = csv.writer(self.file)
        self.output_filepath = filepath
        print('Opened ' + filepath)

    def initialize_hourly_file(self, filepath):
        self.file = open(filepath, 'w') 
        self.writer = csv.writer(self.file)
        self.writer.writerow(['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact','longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity', 'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source', 'retrieval_time'])
        self.output_filepath = filepath
        print('Initialized ' + filepath)

    def write_data(self, input_filepath, output_filepath):
        if not output_filepath == self.output_filepath:
            if not self.file == None:
                self.file.close()
                
            if os.path.isfile(output_filepath):
                self.open_hourly_file(output_filepath)
            else:
                self.initialize_hourly_file(output_filepath)

        try:
            with open(input_filepath) as input_file:
                if input_file.read(6) != '<html>':
                    input_file.seek(0)
                    data = json.load(input_file)
                    for row in data['states']:
                        row.append(data['time'])
                        self.writer.writerow(row)
                else:
                    print('Removing HTML file' + input_filepath)
            os.remove(input_filepath)
        except Exception as e:
            print('Failed ' + input_filepath)
            print(e)
        

json_files = []
for name in os.listdir(root):
    split_path = os.path.splitext(name)
    if split_path[1] == '.json' and 'locations' in split_path[0]:
        json_files.append([split_path[0], os.path.join(root, name)])

json_files = pd.DataFrame(data=json_files, columns=['filename', 'filepath'])
json_files.sort_values(by='filename', inplace=True)

data_writer = DataWriter()
for index, row in json_files.iterrows():
    hourly_filename = row['filename'][10:23] + '.csv'
    hourly_filepath = os.path.join(root, hourly_filename)
    data_writer.write_data(row['filepath'], hourly_filepath)
        
