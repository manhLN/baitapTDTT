n = int(input())
a = str(abs(n))[::-1]
if n < 0:
    a = '-' + a
print(a)