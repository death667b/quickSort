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


    return pivot

print(quick_sort([4, 2, 7, 9, 5, 1, 7]))
