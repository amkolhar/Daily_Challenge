''' This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.'''
import logging


def lowest_postive(arr):
    arr.sort()
    logging.debug(arr)

    for i in range(len(arr)-1):
        if arr[i] < 0:
            pass
        else:
            if arr[i+1] - arr[i] > 1:
                return arr[i] + 1
            else:
                pass

    return arr[-1] + 1


logging.basicConfig(level=logging.DEBUG)
a = [1, 2, 0]
logging.info(lowest_postive(a))

b = [4,5,7,8,12,4,5,-9,0,4,6,7,8,1,2,3,9,10,11]
logging.info(lowest_postive(b))