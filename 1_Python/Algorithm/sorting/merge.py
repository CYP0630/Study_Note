from random import randint
import ipdb

def gen_array(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr


def mergeSort(arr):
    #Divide
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
        return arr

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

arr = gen_array(10, 1, 100)
print(arr)
arr_new = mergeSort(arr)
printList(arr_new)