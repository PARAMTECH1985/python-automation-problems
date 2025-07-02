# Calculate total size of each directory and subdirectory.
filesystem = \
    {
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


for key in filesystem.keys():
    print("Keys details="+key)
    print(filesystem[key])
    for key1 in filesystem[key].keys():
        size1 = 0
        size3 = 0
        print(filesystem[key][key1])
        print(filesystem[key].values())
        for size in filesystem[key].values():
            if type(size) is dict:
                size2 = 0
                for size1 in size.values():
                    size2 = size2 + size1
            else:
                size3=size+size3
                print(filesystem[key])
                if key is not dict:
                    print("Size is="+str(size3))

