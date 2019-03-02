r, s = list(map(int,input().split()))
n = int(input())
groups = []
seating = []
tickets_sold = 0
for i in range(n):
    a = int(input())
    groups.append(a)

for i in range(r):
    seating.append(s)

for size in groups:
    if size > max(seating):
        continue
    else:
        for index, row in enumerate(seating):
            if row >= size:
                seating[index] -= size
                tickets_sold += size
                break
print(tickets_sold)  