"""
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice,
find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

from collections import Counter

lst = [2, 4, 6, 8, 10, 2, 6, 10]

dict_lst = Counter(lst)

answer = []

for key, value in dict_lst.items():
    if value == 1:
        answer.append(key)

print(answer)