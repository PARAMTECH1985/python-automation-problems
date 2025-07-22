def binary_search_algo(item, list=None):
    if list is None:
        list = []
    size = len(list)
    # print(size)
    low = 0
    high = size
    while low <= high:
        mid = low + (high - low) // 2
        if list[mid] == item:
            return mid
        if list[mid] > item:
            high = mid - 1
        if list[mid] < item:
            low = mid + 1
    return -1


list = [10, 20, 30, 40, 50, 60, 70, 80]
item = 60
print(binary_search_algo(item, list))
