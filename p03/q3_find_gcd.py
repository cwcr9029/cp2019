def gcd(m,n):
    small = min([m,n])
    for i in range(small+1,0,-1):
        if m % i == 0 and n % i == 0:
            return i

print(gcd(24, 16))
print(gcd(255,25))