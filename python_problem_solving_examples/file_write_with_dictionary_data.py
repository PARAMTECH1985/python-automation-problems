import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
# Serializing json
json_object = json.dumps(dictionary, indent=4)
# Writing to sample.json
with open("sample1.json", "w") as outfile:
    outfile.write(json_object)
# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

with open("sample2.json", "w") as outfile:
    json.dump(dictionary, outfile,indent=4)

with open("sample3.json", "w") as outfile:
    json.dump(dictionary, outfile)