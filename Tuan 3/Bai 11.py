a, b, c = map(int, input().split())
if a < b + c or b < a + c or c < a + b:
    if a == b == c:
        print("Tam giac deu")
    elif a == b or b == c or a == c:
        print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai tam giac")