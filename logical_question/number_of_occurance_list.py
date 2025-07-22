# Program to count the number of times an element
# Present in the list
def count_occurance(tup, x):
    count = 0
    for ele in tup:
        if ele == x:
            count = count + 1
    return count
# Driver Code
list = [10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2]
enq = 4
enq1 = 10
enq2 = 8
print("Element="+str(enq)+" Found="+str(count_occurance(list, enq))+" Times")
print("Element="+str(enq1)+" Found="+str(count_occurance(list, enq1))+" Times")
print("Element="+str(enq2)+" Found="+str(count_occurance(list, enq2))+" Times")