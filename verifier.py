def is_subset(board, potential_subset):
    def check_subgrid(i, j):
        for di in range(len(potential_subset)):
            for dj in range(len(potential_subset[0])):
                new_i = i + di
                new_j = j + dj
                if potential_subset[di][dj] != board[new_i][new_j]:
                    return False
        return True
    input_m = len(board)
    input_n = len(board[0])
    potential_subset_m = len(potential_subset)
    potential_subset_n = len(potential_subset[0])
    for i in range(input_m - potential_subset_m + 1):
        for j in range(input_n - potential_subset_n + 1):
            if check_subgrid(i, j):
                return True
    return False


def count_surrounding_ones(board, x, y, m, n):
    direc = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0],           [1, 0],
        [-1, 1],  [0, 1],  [1, 1]
    ]
    ones = 0
    for i in range(8):
        new_x = x + direc[i][0]
        new_y = y + direc[i][1]
        if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 1:
            ones += 1
    return ones


def next_generation(curr_board, m, n):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ones = count_surrounding_ones(curr_board, i, j, m, n)
            print(i, j, ones)
            if (curr_board[i][j] and (ones == 2 or ones == 3)) or (not curr_board[i][j] and ones == 3):
                temp[i][j] = 1
    return temp


def verify(input_board, output_board, k, constraint_m, constraint_n):
    curr_board = input_board
    m = len(curr_board)
    n = len(curr_board[0])
    if m > constraint_m and n > constraint_n:
        return False

    while k >= 0:
        if is_subset(curr_board, output_board):
            return True
        curr_board = next_generation(curr_board, m, n)
        k -= 1

    return False


if __name__ == "__main__":

    input_board = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]
    output_board = [[1, 1]]

    k = 119
    constraint_m = 999
    constraint_n = 999
    print(verify(input_board, output_board, k, constraint_m, constraint_n))
