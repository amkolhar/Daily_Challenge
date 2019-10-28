"""
This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""

def max_one_counter(number):
    bin_number = (bin(156).replace("0b", ""))
    print(bin_number)
    counter = 0
    one_count = []
    for i in bin_number:
        if i == "1":
            counter += 1
        else:
            one_count.append(counter)
            counter = 0

    one_count.append(counter)

    return max(one_count)

number = 156
print(max_one_counter(number))