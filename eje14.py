# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE RECIBE FÓRMULAS QUÍMICAS E INFORMA NOMBRE DE LA MISMA ***")

# PROMPTING THE USER
Name = int (input("Ingresar fórmula química:\n1. NaCl.\n2. H2O.\n3. HCI.\n"))
print("")

# PROVIDING THE NAME AS PER INPUT
if Name == 1:
    print("Sal común.")
elif Name == 2:
    print("Agua")
elif Name == 3:
    print("Ácido clorhídrico")