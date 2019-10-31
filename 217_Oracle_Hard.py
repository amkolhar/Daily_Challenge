"""
This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse,
but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.
"""

def decimal_to_binary(dec_number):
    bin_number = bin(dec_number).replace("0b", "")
    # print(bin_number)
    return bin_number


def sparse_binary(bin_number):
    for n in range(len(bin_number)-1):
        if bin_number[n] == "1" and bin_number[n+1] == "1":
            return True
    return False


def find_sparse(dec_number):
    i = True

    while i:
        i = sparse_binary(decimal_to_binary(dec_number))

        if i:
            dec_number += 1

    return dec_number


number = int(input("Number: "))

print(find_sparse(number))




