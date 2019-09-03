"""
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
"""

class BitArray:
    def __init__(self, size):
        self.size = size
        self.bit_array = [None]*size

    def set(self, i, val):
        self.bit_array[i] = val
        return 0

    def get(self, i):
        print(self.bit_array[i])
        return 0

array_one = BitArray(3)
array_one.set(0, 0)
array_one.set(1, 1)
array_one.set(2, 1)
array_one.get(2)

