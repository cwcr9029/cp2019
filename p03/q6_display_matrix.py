import random
num = int(input("Enter an integer: "))
def print_matrix(n):
    for i in range(n):
        for a in range(n):
            print(str(random.randint(0,1)),end=' ')
        print('\n',end='')
print_matrix(num)