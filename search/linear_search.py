def find_item(list, item):
    is_item_found = False
    for i in list:
        if i == item:
            print("Item Found")
            print("Item==" + str(item))
            is_item_found = True
    return is_item_found


list = [1, 2, 3, 5, 10, 20, 40, 60]
item = 20
print(find_item(list, 20))
