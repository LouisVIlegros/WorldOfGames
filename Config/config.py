import json

config = None

with open(r'Config/config.json', 'r') as configuration :
    config = json.load(configuration)