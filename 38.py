thang=input("Nhap ten thang: ")
if thang=="Thang Tu" or thang=="Thang Sau" or thang=="Thang Chin" or thang=="Thang Muoi Mot":
    ngay=30
elif thang=="Thang Hai":
    ngay="28 hoac 29"
else:
    ngay=31
print(thang,"co",ngay,"ngay.")