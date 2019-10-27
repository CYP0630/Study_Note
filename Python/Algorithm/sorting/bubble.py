from random import randint

def gen_array(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr

def bubbleSort(alist):
    n = len(alist)
    exchange = False
    #range(start, stop, step_length)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        if not exchange:
            break
    return alist

arr_1 = gen_array(10, 1, 100)
print(arr_1)
bubble_arr_1 = bubbleSort(arr_1)
print(bubble_arr_1)
