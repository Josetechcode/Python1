# DISPLAY PROGRAM TITLE
print ("*** PROGRAMA QUE CALCULA LA SUMA DE LOS NÚMEROS PARES Y EL PRODUCTO DE LOS NÚMEROS PARES INGRESADOS ***")

Num = int(input("Cuántos números quieres ingresar?: "))

# INITIALIZE VARIABLES AND LISTS TO SAVE THE ENTERED VALUES
i = 0
list_1 = []
list_2 = []

# VALIDING THE AMOUNT OF ENTERED VALUES
while i < Num:
  i+=1
  Num1 = int(input(f"Ingresar número: "))

# CHECKING WHETHER NUMBER ARE EVEN OR ODD
  if Num1 % 2 == 0:
    list_1.append(Num1)
  else:
    list_2.append(Num1)

# DISPLAYING THE EVEN NUMBER LIST AND THE ADDITION
print("Los elementos a sumar son ",list_1,".\nLa suma de los numeros es: ",sum(list_1))

# DISPLAYING THE ODD NUMBER LIST AND CALCULATING THE PRODUCT
product = 1
for x in list_2:
  product *= x
print("Los elementos a multiplicar son: ",list_2,".\nEl producto de los números es: ",product,".")