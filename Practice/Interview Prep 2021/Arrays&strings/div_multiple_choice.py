def equalize(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# print(equalize(2437,875))

def get_sorted_list():
    l = [1,2,9,1,2,3,1,4,1,5,7]
    l = set(l)
    l = list(l)
    l.sort()
    return l

print(get_sorted_list())