# create a nested dictionary with 3 fields of 3 students
data = {
    "documents":
        {
            "resume.pdf": 100,
            "photos":
                {
                    "vacation.jpg": 2000,
                    "family.png": 1500
                }
        },
    "music":
        {
            "song1.mp3": 5000,
            "song2.mp3": 4800
        }
}
for keys in data.keys():
    print(keys)
    print(data[keys])
    print(type(data[keys]))
    if type(data[keys]) is dict:
        print("Key is dictionary")
        for key in data[keys].keys():
            print(data[keys][key])
    else:
        print("Key is not dictionary")