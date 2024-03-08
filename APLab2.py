def find_min_board_size(N, W, H):
    low = 1
    high = max(W, H) * N

    while low < high:
        mid = (low + high) // 2

        row = mid // W
        column = mid // H

        if row * column >= N:
            high = mid
        else:
            low = mid + 1
    return low
