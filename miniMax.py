def minMax(arr):
    # initialize
    min_ = 0
    max_ = 0
    n = len(arr)
    for i in range(n):
        arr.sort()
        min_ = sum(arr[0:n-1])
        max_ = sum(arr[1:])
    print(min_, max_)





