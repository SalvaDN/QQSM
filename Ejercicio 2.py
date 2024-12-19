telefono = (input("Indica tu número de teléfono: "))
caracteres_telefono = len(telefono)

print (" ")

if len(telefono) == 9:
    print("El telefono está bien")
else:
    print("Error al introducir teléfono")

print(" ")
print(f"El numero de telefono {telefono} contine {caracteres_telefono} caracteres")