# def permute(s, s2):
#     if len(s) == 0:
#         print(s2, end=' ')
#         return
#
#     for i in range(len(s)):
#         char = s[i]
#         left_s = s[0:i]
#         right_s = s[i + 1:]
#         rest = left_s + right_s
#         permute(rest, s2 + char)

def reverseString(s):
    stack = []

    # Push the characters into stack
    for char in s:
        stack.append(char)

    # Prepare a list to hold the reversed characters
    rev = [''] * len(s)

    # Pop the characters from stack into the reversed list
    for i in range(len(s)):
        rev[i] = stack.pop()

    # Join the list to form the reversed string
    return ''.join(rev)


s1 = "ABC"
s2 = ""
right_s = ""
left_s = ""
permutation = ""
for i in range(len(s1)):
    # print("Initial String is="+s1)
    for j in range((len(s1) - 1)):
        # new=right_s + left_s
        left_s = s1[0:j + i]
        right_s = s1[j + i:]
        # print(right_s + left_s)
        # s1 = reverseString(s1.join(right_s + left_s))
        # old = right_s + left_s
        if s1 == (right_s + left_s):
            print("String is same")
            s1 = ""
            s1 = reverseString(s1.join(right_s + left_s))
            print(s1)
        # if s1 == (right_s + left_s):
        #     print("String is same")
        #     s1 = ""
        #     s1 = reverseString(s1.join(right_s + left_s))
    # if s1 == (right_s + left_s):
    #     print("Same Found")
    #     s1=reverseString(s1)
    #     print(s1)

fact = 1
number = 3
while number > 0:
    fact = number * fact
    number = number - 1
print(fact)

# def permutation_list(str):
#     for i in range(len(str)):
#         for j in range(len(str)):
#             print(str[0:j + 1])
#
#
# permutation_list('ABC')
# # permutation_list('ABC')
