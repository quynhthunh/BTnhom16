# Nhap tan so:
TanSo=float(input("Nhap tan so: "))
if (261.63-1)<TanSo<(261.63+1):
    Not="C4"
elif (293.66-1)<TanSo<(296.66+1):
    Not="D4"
elif (329.63-1)<TanSo<(329.63+1):
    Not="E4"
elif (349.23-1)<TanSo<(349.23+1):
    Not="F4"
elif (392.00-1)<TanSo<(392.00+1):
    Not="G4"
elif (440.00-1)<TanSo<(440.00+1):
    Not="A4"
elif (493.88-1)<TanSo<(493.88+1):
    Not="B4"
else:
    Not=""
if Not=="":
    print("Tan so khong tuong ung voi not nhac da biet.")
else:
    print(TanSo,"Hz la tan so cua",Not)
