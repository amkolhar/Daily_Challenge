'''This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

'''


a = [5, 1, 1, 5]
sum_list = []

for i in range(len(a)):
    sum = 0
    for j in range(i, len(a), 2):
        sum = sum + a[j]

    sum_list.append(sum)


print(max(sum_list))





