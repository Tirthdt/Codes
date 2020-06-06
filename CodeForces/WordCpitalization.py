s = input()


if 65 <= ord(s[0]) <= 90:
    print(s)
else:
    print(chr(ord(s[0]) - 32) + s[1:])
