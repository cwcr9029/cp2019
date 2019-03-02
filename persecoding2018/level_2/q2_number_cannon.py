rows = int(input())

num_wholes = 0
digits_in_row = 0

for i in range(rows):
    digits_in_row += 1
    num_wholes += digits_in_row

    
print(sum(range(1,num_wholes+1)))