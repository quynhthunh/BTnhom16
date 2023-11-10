ngay=int(input("Nhap ngay: "))
thang=input("Nhap thang: ")
if ngay==1 and thang=="Thang Mot":
    print("Day la ngay dau nam moi.")
elif ngay==1 and thang=="Thang Bay":
    print("Day la ngay Quoc khanh nuoc Canada.")
elif ngay==25 and thang=="Thang Muoi Hai":
    print("Day la ngay le giang sinh.")
else:
    print("Ngay va thang khong hop le. Vui long nhap lai.")