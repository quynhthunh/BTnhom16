n=int(input("Nhập số lượng cạnh (từ 3-10): "))
if 3<=n<=10:
    if n == 3:
        ten_hinh = "Tam giac"
    elif n == 4:
        ten_hinh = "Tu giac"
    elif n == 5:
        ten_hinh = "Ngu giac"
    elif n == 6:
        ten_hinh = "Luc giac"
    elif n == 7:
        ten_hinh = "That giac"
    elif n == 8:
        ten_hinh = "Bat giac"
    elif n == 9:
        ten_hinh = "Cuu giac"
    else:
        ten_hinh = "Thap giac"
    print("Hinh co",n,"canh la hinh",ten_hinh)
else:
    print("Loi, so luong canh phai nam trong khoang tu 3 đen 10.")