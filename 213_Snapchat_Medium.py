"""
This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255.
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123']
"""


def check_if_ip(address):
    ip = address.split(".")

    for i in ip:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False

    return True


def create_ip(code):
    code_len = len(code)
    ip_list = []

    if code_len > 12:
        return ip_list

    code_new = code

    for i in range(1, code_len-2):
        for j in range(i+1, code_len-1):
            for k in range(j+1, code_len):
                code_new = code_new[:k] + "." + code_new[k:]
                code_new = code_new[:j] + "." + code_new[j:]
                code_new = code_new[:i] + "." + code_new[i:]

                if check_if_ip(code_new):
                    ip_list.append(code_new)
                code_new = code

    return ip_list

code = "255401230"

print(create_ip(code))




