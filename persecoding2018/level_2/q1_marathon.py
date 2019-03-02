n = int(input())
name_time_list = []
for i in range(n):
    a = input()
    name, time = a.split(' ')
    name_time_list.append(((list(map(float,time.split(':')))), name))
name_time_list.sort()

position = 0
for t in name_time_list:
    position+=1
    if t[1] == 'Percy':
        print(position)
        break