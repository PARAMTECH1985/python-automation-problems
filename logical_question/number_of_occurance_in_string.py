# Program to count the number of times an element
# Present in the list
def count_occurance(tup, x):
    count = 0
    for ele in tup:
        if ele == x:
            count = count + 1
    return count
# Driver Code
str="abcabcde"
list=list(str)
enq = 'a'
enq1 = 'b'
enq2 ='e'
print(count_occurance(list, enq))
print(count_occurance(list, enq1))
print(count_occurance(list, enq2))