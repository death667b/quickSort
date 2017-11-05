"""
Quick Sort algo in Python3
"""

def quick_sort(arr):
    """
    quick_sort sorts an array of integers.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([4, 2, 7, 9, 5, 1, 7, 1, 43, -5, 1, 76, -3421, 5, 7]))
