
s1 = "ABCD"
s2 = ""
right_s = ""
left_s = ""
permutation = ""
for i in range(len(s1)):
    left_s = s1[0:i]
    right_s = s1[i + 1:]
    print(left_s+right_s)



