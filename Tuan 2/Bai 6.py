a, b, c = map(float,input().split())
if a+b>c or a+c>b or b+c>a:
    d = (a+b+c)/2
    s = (d*(d-a)*(d-b)*(d-c))**0.5
    print(round(s, 1))
else:
    print("khong phai canh tam giac")