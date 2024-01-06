"""
Martha goes to a casino and brings n quarters
number of slots: 3 slot machines (A, B, C)
    - she plays the first
    - the second and third
    - and back to the first.

    Each play costs one quarter
        - Slot machine A pays 30 quarters every 35th time
        - B pays 60 quarters every 100th time
        - C pays 9 quarters every 10th time

Input
    - n: number of quarters. 1<=n<=1000
    - number of times A was played
    - number of times B was played
    - number of time C was played

Output:
    - Martha plays x times before going broke
"""


"""
explore a test case:
    n = 10
    current state
        - A - 28
        - B - 90
        - C - 9
    next state
        play 1
        n - 1
         - A - 29
         - B - 91
         - C - 10
            - n + 9; 10

"""

# enter the number of quarters
n = int(input("Enter the number of quarters: "))

# enter the number of times the play has happpened
machine = 0
plays = 0
first_slot = int(input("Enter the number of plays: "))
second_slot = int(input("Enter the number of plays: "))
third_slot = int(input("Enter the number of plays: "))


while n >= 1:
    n = n - 1
    if machine == 0:
        first_slot += 1
        if first_slot == 35:
            n += 30
    elif machine == 1:
        second_slot += 1
        if second_slot == 100:
            n += 60
    elif machine == 2:
        third_slot += 1
        if third_slot == 10:
            n += 9
    plays += 1
    machine +=1
    if machine == 3:
        machine = 0
   
print(f"Martha plays {plays} times before going broke.")
       








