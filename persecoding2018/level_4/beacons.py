distance = int(input())
n = int(input())
beacons = []
for i in range(n):
    x, y = map(int,input().split())
    beacons.append((x,y))


def calc_distance(point1, point2):
    dist = ((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)**(1/2)
    return dist

start_beacons = [(0,0)]

count = 0
while len(start_beacons) > 0:
    lit_a_beacon = False
    s_beacons = []
    
    for p in start_beacons:
        unlit = beacons[:]        
        for b in unlit:
            if calc_distance(p,b) <= distance:
                lit_a_beacon = True
                s_beacons.append(b)
                beacons.remove(b)
                count += 1
    start_beacons = s_beacons[:]
    if lit_a_beacon:
        print(count)
        