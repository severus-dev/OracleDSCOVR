import json

txt_path = 'kp.txt'
json_path = 'out.json'

data = []

with open(txt_path, 'r') as txt_file:
    for line in txt_file:
        elements = line.split()
        if len(elements) >= 9:
            date = ' '.join(elements[:6])
            planetary_index = float(elements[-3])

            data.append({'date': date, 'planetary_index': planetary_index})

with open(json_path, 'w') as json_file:
    json.dump(data, json_file, indent=2)

