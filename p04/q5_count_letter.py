def count_letter(st,ch):
    if len(st) == 0:
        return 0
    elif st[-1] == ch:
        return count_letter(st[:-1],ch) + 1
    else:
        return count_letter(st[:-1],ch)