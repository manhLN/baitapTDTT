a = input("ten chu ho:")
b = int(input("chi so thang truoc:"))
c = int(input("chi so thang nay:"))
d = c - b
print("ho va ten:", a)
if d <= 50:
    print("so tien phai tra:", round((1984*d)*1.08))
elif 51<= d <= 100:
    print("so tien phai tra:", round((1984*50+2050*(d-50)*1.08)))
elif 101<= d <= 200:
    print("so tien phai tra:", round((1984*50+2050*50+2380*(d-100))*1.08))
elif 201<= d <= 300:
    print("so tien phai tra:", round((1984*50+2050*50+2380*100+2998*(d-200))*1.08))
elif 301<= d <= 400:
    print("so tien phai tra:", round((1984*50+2050*50+2380*100+2998*100+3350*(d-300))*1.08))
else:
    print("so tien phai tra:", round((1984*50+2050*50+2380*100+2998*100+3350*100+3460*(d-400))*1.08))