def sum_digits(n):
    if n // 10 == 0:
        return n
    else:
        a = n % 10
        return a + sum_digits(n // 10)
print(sum_digits(9842))