def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        alist.remove(min(alist))
        return find_largest(alist)
find_largest([2,3,4,100,5,7,90])