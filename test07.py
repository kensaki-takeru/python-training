tk = 0

def thu(tk):
    thu = float(input("Nhap so tien thu: "))
    tk += thu
    # same as tk = thu + thu
    return tk

def chi(tk):
    chi = float(input("nhap so tiem chi: "))
    tk -= chi
    # tk = chi - chi
    return tk

while True:
    a = input("Nhap lua chon: ")

    if a.lower() == "thu":
        tk = thu(tk)
        print(f"So tk sau khi thu : {tk}")
    elif a.lower() == "chi":
        if tk != 0:
            tk = chi(tk)
            print(f"so tai khoan sau khi chi; {tk}")
        else:
            print("tai khoan khong du:>>>")