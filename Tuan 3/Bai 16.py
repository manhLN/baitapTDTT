n = float(input())
if n == int(n):
    print(n, n, n)
else:
    if n > 0:
        print(int(n + 1), int(n), int(n + 1)) if n - int(n) >= 0.5 else print(int(n + 1), int(n), int(n))
    else:
        print(int(n), int(n-1), int(n-1)) if n - int(n) <= -0.5 else print(int(n), int(n-1), int(n))