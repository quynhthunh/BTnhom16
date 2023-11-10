n=int(input("Nhap tuoi nguoi: "))
if (0<=n<=2):
    tc=n*10.5
    print(n,"nam tuoi nguoi bang",round(tc),"nam tuoi cho")
elif n>2:
    tc=2*10.5+(n-2)*4
    print(n,"nam tuoi nguoi bang",round(tc),"nam tuoi cho")
elif n<0:
    print("Nhap sai, so tuoi nguoi phai lon hon 0")
