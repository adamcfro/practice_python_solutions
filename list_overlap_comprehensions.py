a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = list(set([num for num in a if num in b]))
print(new_list)



#########

from random import sample

a = sample(range(1, 30), 12)
b = sample(range(1, 30), 16)
result = [i for i in set(a) if i in b]
print(result)