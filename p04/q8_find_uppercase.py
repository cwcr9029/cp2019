def find_num_uppercase(st):
    if len(st) == 0:
        return 0
    if 65 <= ord(st[0]) <= 90:
        return find_num_uppercase(st[1:]) + 1
    else:
        return find_num_uppercase(st[1:])
print(find_num_uppercase('DID YOU KNOW THAT I HAVE FORTY FOUR UPPERCASE LETTERS'))