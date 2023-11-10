n=float(input("Nhap muc do tieng on: "))

# Xác định kết quả dựa trên giá trị mà người dùng nhập
if n==130:
    print("Muc do tieng on la: Bua khoan (Jackhammer)")
elif n==106 :
    print("Muc do tieng on la: May cat co (Gas lawnmower)")
elif n==70:
    print("Muc do tieng on la: Dong ho bao thuc (Alarm clock)")
elif n==40:
    print("Muc do tieng on la: Phong yen tinh (Quiet room)")
elif 40<n<70:
    print("Muc do tieng on nam giua: Phong yen tinh (Quiet room) va Dong ho bao thuc (Alarm clock)")
elif 70<n<106:
    print("Muc do tieng on nam giua: Dong ho bao thuc (Alarm clock) va May cat co (Gas lawnmower)")
elif 106<n<130:
    print("Muc do tieng on nam giua: May cat co (Gas lawnmower) va Bua khoan (Jackhammer)")
else:
    print("Muc do tieng on khong nam trong khoang muc do da cho.")
