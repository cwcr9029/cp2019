def m_series(i):
    result = 0
    numerator = i
    
    while numerator >= 1:
        denominator = numerator + 1
        result += numerator / denominator
        numerator -= 1
    return result
print('i\t\tm(i)')
for num in range(1,21):
    print('{0}\t\t{1:.4f}'.format(num,m_series(num)))