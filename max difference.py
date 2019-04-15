def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]

    for i in range(0, arr_size):
        for j in range(i + 1, arr_size):
            if (arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]

    return max_diff


# Driver program to test above function
arr = [1, 2, 90, 10, 110]
size = len(arr)
print("Maximum difference is", maxDiff(arr, size))