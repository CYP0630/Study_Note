from random import randint
import ipdb

def gen_array(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr

def insertSort(alist):
    #We assume the first is correct
    #Start from the second position
    ipdb.set_trace()
    for i in range(1, len(alist)):
        current_position = alist[i]
        position_idx = i
        while alist[position_idx -1] > current_position and position_idx > 0:
            alist[position_idx] = alist[position_idx - 1]
            # Compare the current with previous elements
            position_idx = position_idx - 1
        alist[position_idx] = current_position
    return alist

arr_1 = gen_array(10, 1, 100)
print(arr_1)
insertSort_arr_1 = insertSort(arr_1)
print(insertSort_arr_1)
