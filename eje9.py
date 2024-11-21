# DISPLAY PROGRAM TITLE
print ("*** PROGRAMA QUE CALCULA LA SUMA DE LOS NÚMEROS PARES Y EL PRODUCTO DE LOS NÚMEROS PARES INGRESADOS ***")

Num = int(input("Cuántos números quieres ingresar?: "))

i = 0
list_1 = []
list_2 = []
while i < Num:
  i+=1
  Num1 = int(input(f"Ingresar número: "))
  
  if Num1 % 2 == 0:
    list_1.append(Num1)
  else:
    list_2.append(Num1)

print("Los elementos a sumar son ",list_1,".\nLa suma de los numeros es: ",sum(list_1))

product = 1
for x in list_2:
  product *= x
print("Los elementos a multiplicar son: ",list_2,".\nEl producto de los números es: ",product,".")