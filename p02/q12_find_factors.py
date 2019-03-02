num = int(input("Enter an integer: "))
factor_list = []
prime_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
while num != 1:
    for i in range(1,num+1):
        if i in prime_list and num % i == 0:
            num = int(num/i)
            factor_list.append(i)

factor_list.sort()
for n in factor_list:
    print(n,end=' ')