"""
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string.
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7]
"""

given_str = "abracadabrabrarb"
pattern_str = "abr"

pattern_len = len(pattern_str)
index_list = []

for n in range(len(given_str) - pattern_len+1):
    sample_str = given_str[n:n+pattern_len]
    if sample_str == pattern_str:
        index_list.append(n)

print(index_list)