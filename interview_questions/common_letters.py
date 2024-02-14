"""
Write a Python Program to
find out common letters between
two strings

e.g:
    1.) NAINA
    2.) REENE

Decompose the problem:
    - string 1
    - string 2

"""
def common_letters():
    str1 = input("Enter the string 1: ")
    str2 = input("Enter the string 2: ")

    # to get unique letters
    s1 = set(str1)
    s2 = set(str2)

    # elements in s1 and s2
    lst = s1 & s2

    print(lst)


