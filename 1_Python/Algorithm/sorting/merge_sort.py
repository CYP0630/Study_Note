
def merge_sort(array):
    merge_sort_helper(array, 0, len(array) - 1)

def merge_sort_helper(array, left, right):
    if left >= right:
        return
    mid = (left + right) // 2 #[left, mid] [mid+1, right]
    
    merge_sort_helper(array, left, mid)
    merge_sort_helper(array, mid+1, right)
    merge(array, left, right)

def merge(array, left, right):

    n = right - left + 1
    tmp = [0 for _ in range(n)]

    mid = (left + right ) // 2
    i, j = left, mid + 1

    for k in range(n):
        if i<=mid and (j > right or array[i] <= array[j]):
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1

    for k in range(n):
        array[left + k] = tmp[k]
    
    
if __name__ == '__main__':
    array = [6, 4, 5, 7, 2, 4, 3, 4, 7, 8]
    merge_sort(array)

    for num in array:
        print(num, end=' ')
    print()
