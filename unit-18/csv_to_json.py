import csv
import json


def make_json(csv_file, json_file):
    data = {}
    
    with open(csv_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for rows in reader:
            key = rows['id']
            data[key] = rows
    
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))
        
make_json('blogger.csv', 'blogger.json')
        
