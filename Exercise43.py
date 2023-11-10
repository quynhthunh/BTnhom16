tien=int(input("Nhap vao menh gia tien: $"))
if tien==1:
    ten="George Washington"
elif tien==2:
    ten="Thomas Jefferson"
elif tien==5:
    ten="Abraham Lincoln"
elif tien==10:
    ten="Alexander Hamilton"
elif tien==20:
    ten="Andrew Jackson"
elif tien==50:
    ten="Ulysses S. Grant"
elif tien==100:
    ten="Benjamin Franklin"
else:
    ten=""

if ten=="":
    print("Khong hop le.")
else:
    print("Ong ",ten," xuat hien tren to $",tien,".",sep="")
