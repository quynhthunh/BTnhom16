# Nhap ten not nhac:
ten=input("Nhap ten not nhac: ")
Not=ten[0]
QuangTam=int(ten[1])
if Not=="C":
    TanSo=261.63
elif Not=="D":
    TanSo=293.66
elif Not=="E":
    TanSo=329.63
elif Not=="F":
    TanSo=349.23
elif Not=="G":
    TanSo=392.00
elif Not=="A":
    TanSo=440.00
elif Not=="B":
    TanSo=493.88
TanSo=TanSo/2**(4-QuangTam)
print("Tan so cua",ten,"la",TanSo,"Hz.")