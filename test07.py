# variable, use test02.py
tk = 0

# def, use test03.py
def thu(tk):
    thu = float(input("Nhap so tien thu: "))
    # increment, use test06.py
    tk += thu
    # same as tk = tk + thu
    return tk

def chi(tk):
    chi = float(input("nhap so tiem chi: "))
    # decrement, use test06.py
    tk -= chi
    # tk = tk - chi
    return tk

# while is a loop by Python. please check it later
while True:
    a = input("Nhap lua chon: ")
    # if is condition. if -> elif or if -> else. please check it later
    if a.lower() == "thu":
        tk = thu(tk)
        print(f"So tk sau khi thu : {tk}")
    elif a.lower() == "chi":
        if tk != 0:
            tk = chi(tk)
            print(f"so tai khoan sau khi chi; {tk}")
        else:
            print("tai khoan khong du:>>>")