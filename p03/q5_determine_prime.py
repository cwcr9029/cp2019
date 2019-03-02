import math
def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

primes = []
n = 2
while len(primes) < 1000:
    if is_prime(n):
        primes.append(n)
    n += 1
for index in range(1000):
    print(str(primes[index]),end='\t')
    if (index+1) % 10 == 0:
        print('\n')