# How to update a JSON file in Python

import json

file_path = 'employees.json'

with open(file_path, 'r', encoding='utf-8') as json_file:
    employees_list = json.load(json_file)

print(employees_list)

employees_list[1]['name'] = 'Bobby Hadz'
print(employees_list[1])

with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(employees_list, json_file)
    print('JSON file updated successfully')