def permute(s, path=""):
    # Base case: If the string 's' is empty
    # print the current permutation stored in 'path'
    if not s:
        print(path)
        return
    # Loop through each character in the string 's'
    # for i in range(len(s)):
    #     print(s[:i]+s[i + 1:]+s[i])
    for i in range(len(s)):
        permute(s[:i] + s[i + 1:], path + s[i])
s = "abc"
permute(s)