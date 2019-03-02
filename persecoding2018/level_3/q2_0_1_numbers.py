num = int(input())

def get_permutations(n):
     if n == 0:
          return [0,1]
     permutations = []
     permutations.extend(get_permutations(n-1))
     for num in get_permutations(n-1):
          permutations.append(10**n + num)
     return permutations

def find_divisible_01number(num):
     x = 1
     while True: 
          permutations = get_permutations(x)[2:]
          for i in permutations:
               if i % num == 0:
                    return(i)
          x += 1
print(find_divisible_01number(num))

