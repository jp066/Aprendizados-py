def left_rotation(arr, d):
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]

arr = [1, 2, 3, 4, 5]
d = 4
print(left_rotation(arr, d))  # [5, 1, 2, 3, 4]