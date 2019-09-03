"""
This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i,
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them.
If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""


# Ques Array
ques_list = [4, 7, 8, 5, 3, 5, 6, 4]

# Input index
a = 4


index_value = ques_list[a]

list_max = max(ques_list)

# print(list_max)
i = index_value
answer_index_list = []

while i <= list_max:
    i += 1
    if i in ques_list:
        for j, value in enumerate(ques_list):
            if value == i:
                answer_index_list.append(j)
        break

list_diff = []
for k in answer_index_list:
    list_diff.append(abs(k-a))

answer_index = answer_index_list[list_diff.index(min(list_diff))]

print(answer_index)










