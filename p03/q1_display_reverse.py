def reverse_int(n):
    num = str(n)
    li = [i for i in num]
    li.reverse()
    return ''.join(li)
print(reverse_int(1234567890))