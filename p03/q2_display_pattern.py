def display_pattern(n):
    s = ''
    b = []
    for i in range(n,0,-1):
        s += str(i) + ' '
    max_length = len(s)
    for i in range(1,n+2):
        s = ''
        for a in range(1,i):
            if a < i-1:
                s += str(a)+' '
            else:
                s += str(a)
        s+='\n'
        
        if len(s) < max_length:
            b.append(' ' * (max_length-len(s)))
        b.append(s)
    print(''.join(b))
display_pattern(101)