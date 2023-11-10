c1 = float(input("Nhap do dai canh 1: "))
c2 = float(input("Nhap do dai canh 2: "))
c3 = float(input("Nhap do dai canh 3: "))
if (c1==c2==c3):
    print("Day la tam giac deu")
elif (c1==c2 or c1==c3 or c2==c3):
    print("Day la tam giac can")
else:
    print("Day la tam giac thuong")