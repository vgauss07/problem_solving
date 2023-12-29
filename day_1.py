"""
Parking Space Challenge
Input: 
    - the first line contains integer n, the number of parking spaces
       1 <= n <= 100
    - the second line contains a string of n characters for yesterday's
      information, one character for each parking space. 
       C - car
       e - empty
      e.g: CCe (2 occupied parking spaces, and the third is empty)
Output:
    - output the number of parking spaces that were occupied on both 
      days

"""
n = int(input()) # total parking spots
parking = input("Enter parking information: ")
occupied = 0
empty = 0


for i in range(len(parking)):
    if parking[i] == "C" and parking[i+1] == "C":
        occupied += 1
    elif parking[i] == "e":
        empty += 1
print(f'Number of occupied parking spaces on both days: {occupied}')
print(f'Number of empty spaces: {empty}')

