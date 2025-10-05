a, b = map(int, input().split())
print("Vo nghiem") if a == 0 and b != 0 else(print("Vo so nghiem") if a == 0 and b == 0 else print(round(-b / a, 2)))
