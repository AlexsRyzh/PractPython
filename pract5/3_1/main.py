import deal


@deal.pre(lambda arr, x: type(arr) == type([]) and type(x) == type(0))
@deal.post(lambda result: result > -1)
@deal.ensure(lambda arr, x, result: result == arr.index(x))
@deal.raises(ZeroDivisionError)
@deal.reason(ZeroDivisionError, lambda arr: True)
@deal.has()
def binary_search(arr, x):
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
