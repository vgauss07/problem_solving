# Anagram
from collections import Counter

str_1 = 'below'
str_2 = 'elbow'

print('anagram') if Counter(str_1) == Counter(str_2) else print("not an anagram")