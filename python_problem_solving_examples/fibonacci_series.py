# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))
# first two terms
n1=0
n2 =1
count = 0
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1,end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count = count+1
