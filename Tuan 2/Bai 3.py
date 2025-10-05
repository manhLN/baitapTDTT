a = input()
x = ord(a)
if 65 <= x <= 90:
    print(chr(x + 32))
else:
    print(chr(x - 32))