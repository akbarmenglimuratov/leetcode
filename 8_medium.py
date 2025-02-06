# SOLVED
import string


def myAtoi(text):
    text = text.strip()

    if not text:
        return 0

    sign = -1 if text[0] == '-' else 1
    text = text[1:] if text[0] in ['-', '+'] else text
    res = 0

    for char in text:
        if not char.isdigit():
            break

        res = res * 10 + int(char)

        if res * sign < -2 ** 31:
            return -2 ** 31
        if res * sign > 2 ** 31 - 1:
            return 2 ** 31 - 1

    return res * sign


# s = "-4193- with words"
# s = '-000-912 sdf 8 sdf s3df472332sdf'
s = input()
print(myAtoi(s))
