import math

arr = [1, 2, 3, 4, 5]
def miniMaxSum(z):
    max_s= sum(arr[1:])
    mini_s= sum(arr[:-1])
    b = max(arr)
    z = min(arr)
    arr.clear()

    # x = [mini_s, max_s]
    print(max_s, mini_s, b, z, arr)
    # return mini_s, max_s

miniMaxSum(arr)
