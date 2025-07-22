# Calculate total size of each directory and subdirectory.
# def recursion_method(dictionary):
#     for key in dictionary.keys():
#         print("Print main key")
#         print(key)
#         return key
def iterate_nested_dict(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            iterate_nested_dict(value)
        else:
            print(f"Key={key} and value={value}")
nested_dict = \
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

iterate_nested_dict(nested_dict)
