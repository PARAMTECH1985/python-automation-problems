import json

try:
    with open("sample.json", "r", encoding="utf-8") as config_file:
        data = json.load(config_file)
        print(data)
except FileNotFoundError:
    print("File not found: my_file.json")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")