import json
import csv
with open('/media/data/shared/adsb/locations_2021_02_24_01_32_46.json') as file:
    data = json.load(file)
    with open('out.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact','longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity', 'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source', 'retrieval_time'])
        for row in data['states']:
            row.append(data['time'])
            writer.writerow(row)
