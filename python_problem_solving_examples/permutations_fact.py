def permute(s1, s2):
    if len(s1) == 0:
        print(s2, end=' ')
        return

    for i in range(len(s1)):
        char = s1[i]
        left_s = s1[0:i]
        right_s = s1[i + 1:]
        new_str = left_s + right_s
        permute(new_str, s2 + char)


s1 = "ABCD"
s2 = ""
permute(s1, s2)
