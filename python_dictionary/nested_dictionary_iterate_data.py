# create a nested dictionary with 3 fields of 3 students
data = {
    'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
    'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
    'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
}
for i in data:
    print(data[i].items())
    for key,values in data[i].items():
        print("Key="+str(key))
        print("Values="+str(values))