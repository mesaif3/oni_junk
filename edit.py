from json import loads, dumps
import pprint

file_name = "pet gen temp.json"
with open(file_name, 'r') as file:
    for row in file:
        blueprint = loads(row)

for block in blueprint['buildings']:
    if block['offset']['x'] < 8:
        block['offset']['y'] -= 8
blueprint['friendlyname'] = "pet gen temp sihfted"
with open('text.json', 'w') as jsontext:
    jsontext.write(dumps(blueprint))
with open('text.txt', 'w') as text:
    pprint.pprint((blueprint),stream=text)
