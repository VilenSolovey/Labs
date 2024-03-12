def is_arr_monotonic(arr):
    N = len(arr)
    increasing = False
    decreasing = False

    if N == 1:
        return True
    for i in range(1, N):
        if arr[i] < arr[i - 1]:
            decreasing = True

    for i in range(1, N):
        if arr[i] > arr[i - 1]:
            increasing = True

    if increasing and decreasing:
        return False
    return True

