# number guessing game
# logarithmic time O(log(n)) complexity
# step 1
def binary_search(list_items, choice_value):
    first = 0
    last = len(list_items) - 1
    found_ = False
    # since we don't know how many times we
    # are going to loop we use the while loop
    # instead of for loop
    while (first <= last and not found_):
        midpoint = (first + last) // 2
        if list_items[midpoint] == choice_value:
            found_ = True
        else:
            if list_items[midpoint] > choice_value:
                last = midpoint - 1
            else:
                first = midpoint + 1