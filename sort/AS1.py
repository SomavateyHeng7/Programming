# Linear search implementation
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Bidirectional search implementation
def bidirectionSearch(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] == x:
            return left
        elif arr[right] == x:
            return right
        left += 1
        right -= 1
    return -1

def fourslicebidirectionSearch(arr, x):
    n = len(arr)
    slice_len = n // 4
    left, mid_left, mid_right, right = slice_len, slice_len*2, slice_len*3, n-slice_len
    left_slice = arr[:left]
    mid_left_slice = arr[left:mid_left]
    mid_right_slice = arr[mid_left:mid_right]
    right_slice = arr[mid_right:right]

    # apply bidirectional search on each slice
    result = linearSearch(left_slice, x)
    if result != -1:
        return result

    result = bidirectionSearch(mid_left_slice, x)
    if result != -1:
        return left + result

    result = bidirectionSearch(mid_right_slice, x)
    if result != -1:
        return mid_left + result

    result = linearSearch(right_slice, x)
    if result != -1:
        return mid_right + result

    # if element not found
    return -1
