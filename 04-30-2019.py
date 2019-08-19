"""This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers,
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2"""


a = [2, 1, 5, 7, 2, 0, 5]

for i in range(len(a)):
    b = sorted(a[:i+1])
    if len(b) % 2 == 0:
        tot = b[len(b)//2 - 1] + b[len(b)//2]
        median = tot / 2
    else:
        median = b[len(b)//2]
    print(median)


