# dictionary

customer = {"Name":"Eko", "Age":30, "Address":"Bekasi"}

name = customer["Name"]
age = customer["Age"]
adress = customer["Address"]

customer["Company"] = "X"
customer["Name"] = "Anandela"

del customer["Name"]

for key, value in customer.items():
    print(f"{key}:{value}")