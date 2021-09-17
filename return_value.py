# def jumlahkan(satu, dua, tiga=0):
#     total = satu + dua + tiga
#     print(f"Total {[satu, dua, tiga]} = {total}")

# jumlahkan(10, 10, 10)

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(angka)
    print(f"Total {list_angka} = {total}")
    return (list_angka, total)
    
list_angka, total = jumlahkan(10, 50, 30)

print(f"Total {list_angka} = {total}")