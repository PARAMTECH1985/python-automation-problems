l1 = ["foo", "bar", "test"]  # first name
l2 = [22, 33, 44]  # id
l3 = ["rr", "tt", "mm"]  # last name


# Assumaption, len(l1, l2, l3) are same
def print_combined_list1(combined_list):
    for keys in combined_list.keys():
        # print(f'Full Name is={details['Full_Names']}')
        # print(f'and id is={str(details['Ids'])}')
        if keys == 'Full_Names':
            for values in combined_list[keys]:
                print(f'Full Name is={values}')
        if keys == 'Ids':
            for values in combined_list[keys]:
                print(f'Id is={values}')


class CombineList:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def combine_list(self):
        combine_list = {"Full_Names": [], "Ids": []}
        length = len(l1)
        count = 0
        while count < length:
            if len(combine_list) == 0:
                combine_list["Full_Names"] = f"{l1[count]} {l3[count]}"
                combine_list["Ids"] = f"{l2[count]}"
            else:
                combine_list["Full_Names"].append(f"{l1[count]} {l3[count]}")
                combine_list["Ids"].append(l2[count])
            count = count + 1
        return combine_list

    def print_combined_list2(self, combined_list):
        for keys, values in combined_list.items():
            if keys == 'Full_Names':
                for value in values:
                    print(f'Full Name is={value}')
            if keys == 'Ids':
                for value in values:
                    print(f'Id is={value}')


l1 = ["foo", "bar", "test"]  # first name
l2 = [22, 33, 44]  # id
l3 = ["rr", "tt", "mm"]  # last name
combine_list_object = CombineList(l1, l2, l3)
combine_list = combine_list_object.combine_list()
print_combined_list1(combine_list)
combine_list_object.print_combined_list2(combine_list)
