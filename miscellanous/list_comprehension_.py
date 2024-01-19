## Data (daily stock prices ($))
"""
Create a new sample data that
picks every other element

"""
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

# One - Liner
sample = [line[::2] for line in price]


# Result
print(sample)


# Remove corrupted data

"""
Replace every other string with the 
string immediately in fron it.
"""
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

visitors[1::2] = visitors[::2]

# Result
print(visitors)


## Analyzing Cardiac Health Data with List Concatenation
"""
Monitor and visualize the health statistics of patients by
tracking their cardiac cycles
"""

import matplotlib.pyplot as plt

# Data
cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

# Remove the redundant values; [62]

# One-Liner
expected_cycles = cardiac_cylce[1:-2] * 10

# Result
plt.plot(expected_cycles)
plt.show()

## Generators
"""
using generators expressions to find companies
that pay below minimum wage.

instead of:
 sum([x*x for x in range(20)])
 sum(x*x for x in range(20))
"""
# Data
companies = {
    'CoolCompany' : {'Alice': 33, 'Bob': 28, 'Frank': 29},
    'CheapCompany' : {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
    'ShoeCompany' : {'Esther': 38, 'Cole': 8, 'Paris': 18}
}
# One-Liner
illegal_ = [x for x in companies if any(y<9 for y in companies[x].values())]

print(illegal_)