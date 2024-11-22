# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE CONVIERTE DE GRADOS A RADIANES Y VICEVERSA*** ")

# PROMPT THE USER WHAT CONVERSION THEY WANT TO DO
Conver = 0
while Conver != 1 and Conver != 2:
    Conver = int(input("Qué operación quiere realizar?:\n1. Grados a radianes.\n2. Radianes a grados.\n"))

# PROMPT THE USER THE VALUE EN CALCULATING THE NEW VALUE
if Conver == 1:
    valor = int(input("Ingresa el valor en grados: "))
    print("El valor en radianes es: ",valor * 3.1416/180," rad")
else:
    valor = int(input("Ingresa el valor en radianes: "))
    print("El valor en grados es: ",valor * 180/3.1416," grados")