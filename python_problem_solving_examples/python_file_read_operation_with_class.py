import json


class FileOperations:
    def __init__(self,file_name):
        print("Initialization of Properties")
        self.file_name=file_name

    def read_json_file_content(self):
        data=""
        with open(self.file_name, 'r',encoding="utf-8") as file:
            data = json.load(file)
        # print(data)
        return data


file = FileOperations("sample1.json")
print(file.read_json_file_content())
