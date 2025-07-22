s = "abc"
# Initialize an empty list to store the permutations
res = []
# Use three nested loops to generate all possible combinations of indices
# The outermost loop iterates through each character in the string
for i in range(len(s)):
    # The middle loop iterates through each character for the second position
    for j in range(len(s)):
        # The innermost loop iterates through each character for the third position
        for k in range(len(s)):
            if i != j and j != k and k != i:
                res.append(s[i] + s[j] + s[k])
print(res)