def binary_search():
    arr = [1, 2, 3, 4, 5]
    x = input()
    left = 0
    right = len(arr)
    while left <= right:
        mid = round((left + right) / 2)
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return -1
