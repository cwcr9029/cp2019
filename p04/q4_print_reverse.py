def reverse_int(n):
    s = str(n)
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_int(int(s[:-1]))
print(reverse_int(1231234))