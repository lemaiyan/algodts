"""
Given an array return a the largest number that can be possibly get.
for example given [2, 6, 8, 30, 34, 7, 98] it should return 9887634302 as
string to avoid overflow issues
"""

def largest_number(arr):
    merge_sort(arr)
    print(arr)
    return "".join(arr)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        left_str = str(left[i])
        right_str = str(right[j])
        # we reverse the merge sort also we campare the numbers as strings
        # in python '6' > '34' returns True
        if left_str > right_str:
            arr[k] = left_str
            i += 1
        else:
            arr[k] = right_str
            j += 1
        k += 1

    while i < len(left):
        arr[k] = str(left[i])
        i += 1
        k += 1

    while j < len(right):
        arr[k] = str(right[j])
        j += 1
        k += 1
