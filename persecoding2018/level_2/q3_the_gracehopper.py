stunt = input()
li = [x for x in stunt]

speed = (li.count('+') * 5 + li.count('-')) * 3
speed_needed = li.count('#') * 4

if speed >= speed_needed:
    print('\\')
else:
    print((int(speed//4)+1)*'#')