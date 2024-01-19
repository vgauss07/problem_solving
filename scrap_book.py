i =  [1, 2, 3,
     4, 5, 6,
     9, 8, 9]

"""
left_to_right_diagonal:
    1 + 5 + 9 = 15
right_to_left_diagonal:
    3 + 5 + 9 = 17
Find absolute value:
|15 - 17| = 2
"""

def diagonal_difference(arr):
    ldiagonal = rdiagonal = 0
    for i in range(n):
        ldiagonal += arr[i][i]
        rdiagonal += arr[i][n-1-1]
    return abs(ldiagonal-rdiagonal)