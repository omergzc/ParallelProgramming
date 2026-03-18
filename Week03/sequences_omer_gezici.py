def remove_duplicates(seq: list) -> list:
    for i in seq.copy():
        a = seq.count(i) - 1
        while a>0:
            seq.remove(i)
            a-=1
    return seq.copy()

print(remove_duplicates([1, 2, 3, 3, 4, 5, 5, 5, 6]))
print(remove_duplicates([1, 2, 3, 4, 5, 6]))
print(remove_duplicates([1, 1, 1, 1, 1, 1]))
print(remove_duplicates([]))

def list_count(seq: list) -> dict:
    dict_a = {}
    for i in seq:
        dict_a[i] = seq.count(i)
    return dict_a

print(list_count([1, 2, 3, 3, 4, 5, 5, 5, 6]))
print(list_count([1, 2, 3, 4, 5, 6]))
print(list_count([1, 1, 1, 1, 1, 1]))
print(list_count([]))

def reverse_dict(d: dict) -> dict:
    dict_b = {}
    for i,j in d.items():
        dict_b[j] = d.get(j,i)
    return dict_b

print(reverse_dict({1: 1, 2: 2, 3: 3}))
print(reverse_dict({1: 2, 2: 3, 3: 4}))
print(reverse_dict({1: 1, 2: 1, 3: 1}))
print(reverse_dict({}))
