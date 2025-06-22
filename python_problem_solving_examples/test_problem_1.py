my_list = [1, 2, 3, 4, 5, 6, 7]
rotate_num_of_elements = 2
expected_list = [2, 1, 4, 3, 6, 5, 7]
new_list = []
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# rotate_num_of_elements = 3
# expected_list = [3, 2, 1, 6, 5, 4, 7, 8]
pair = len(my_list)//2
print(pair)
# count = 0
# for item in my_list:
#     print(item)
#     if count < list_size // 2:
#         my_list.pop(count)
#         my_list.pop(count + 1)
#         count = count + 1
print(my_list)
count=0
for item in my_list:
    temp_list=[]
    if count<pair:
        temp_list=my_list[:2]
print(temp_list)




# a=30
# b=60
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# length_list = len(my_list) - 1
# print(length_list)
# length_list //= 2
# pair = length_list
# print(length_list)
# for i in my_list:
#     count = 0
#     # print(i)
#     if (length_list > 0):
#         my_list[count] = my_list[count + 1]
#         my_list[count + 1] = my_list[count]
#
# print(my_list)
#
# my_list = [1, 2, 3, 4, 5, 6, 7]
# rotate_num_of_elements = 2
# expected_list = [2, 1, 4, 3, 6, 5, 7]
# # my_list.pop(0)
# # my_list.insert(1,my_list[1])
# print(my_list)
# new_list = []
# temp = a; 
#   a = b;   // Assign the value of 'b' to 'a'
#   b = temp; // Assign the value of 'temp' (which is the original 'a') to 'b'
# def swap_element(list):
#     temp=list[0]


# new_list = []
# list_size = len(my_list)
# print(list_size)
# for item in my_list:
#     my_list.pop(index)


# #INSERT
# #SEARCH
# #DELETE
# class LinkListOperations:

#     def __init__(self):
#         print("Intitialization")

#     def insert(self,number,list):
#         count=0
#         for i in list:
#             print(i)
#             count=count+1
#         list.insert(count,number)
#         return list
#     def search(self,number,list):
#         count=0
#         for i in list:
#             print(i)
#             if(i==number):
#                 print("Number Found")
#                 print("Number Position="+str())
#                 count=count+1
#         return count        

#     def delete(self,number,list):
#         count=0
#         for i in list:
#             print(i)
#             count=count+1
#             if(i==number):
#                 print("Number Found and need to remove the number")
#                 list.pop(count)    
#                 print(list)

# l=LinkListOperations()
# list=[1,2,3,4,5,6,7,8]
# number=8
# l.delete(number,list)
