"""
Slot machines with %
"""
quarter = int(input())
first_slot = int(input())
second_slot = int(input())
third_slot = int(input())

machine = 0
plays = 0 

while quarter >= 1:
    machine = plays % 3
    quarter = quarter - 1

    if machine == 0:
        first_slot += 1
        if first_slot % 35 == 0:
            quarter += 30
    elif machine == 1:
        second_slot += 1
        if second_slot % 100 == 0:
            quarter += 60
    elif machine == 2:
        third_slot += 1
        if third_slot % 10 == 0:
            quarter += 9
    plays += 1

    if machine == 3:
        machine = 0

print(f"Martha plays {plays} times before going broke")
