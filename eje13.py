# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE INFORMA EL DESCUENTO SEGÚN LA MEMBRESIA ***")

# PROMPTING THE USER THE MEMBERSHIP
member = input("Ingresar tipo de membresía: ")

# DISPLAYING THE DISCOUNT AS PER ENTERED MEMBERSHIP
if member == 'A':
    print ("Corresponde un descuento en la compra de 10%.")

elif member == 'B':
    print ("Corresponde un descuento en la compra de 15%.")

elif member == 'C':
    print ("Corresponde un descuento en la compra de 20%.")