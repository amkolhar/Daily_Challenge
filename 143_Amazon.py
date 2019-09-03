"""
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""

lst = [9, 12, 3, 5, 14, 10, 10]
x = 10

equal_lst = []
less_lst = []
more_lst = []

for i in lst:
    if i == x:
        equal_lst.append(i)
    elif i < x:
        less_lst.append(i)
    else:
        more_lst.append(i)

print(equal_lst)
print(less_lst)
print(more_lst)