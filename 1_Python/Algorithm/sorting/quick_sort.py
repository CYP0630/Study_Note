from random import randint

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, left, right):
    if left >= right:
        return

    pivot = array[(left + right) // 2]

    i, j = left, right

    while i<=j:
        while i <= j and array[i] < pivot:
            i += 1

        while i <= j and array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    quick_sort_helper(array, left, j)
    quick_sort_helper(array, i, right)


array = [6, 4, 5, 7, 2, 4, 3, 4, 7, 8]

quick_sort(array)
for num in array:
    print(num, end = ' ')
print()


