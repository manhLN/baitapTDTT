a, b, c, d = map(int, input().split())
largest_num = a
if b > a:
    largest_num = b
if c > b:
    largest_num = c
if d > c:
    largest_num = d
print(largest_num) 