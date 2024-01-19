def find_median(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]


lst = [1, 8, 9, 2, 4, 5, 7]

print(find_median(lst))


# Given an array of integers, where all elements but one occur twice, find the unique element.
def lonely_integers(a):
    for i in a:
        if a.count(i) == 1:
            return i

#return [i for i in a if a.count(i) == 1][0]