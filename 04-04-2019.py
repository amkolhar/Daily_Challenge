'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

import string
from collections import OrderedDict

alpha_map = OrderedDict({k: v for k, v in zip(range(1, 27), string.ascii_lowercase)})
print((alpha_map))

def decoding(msg):
    message = ''
    msg_list = []
    while True:


    print(alpha_map[int(msg[0:2])])




decoding('111')





