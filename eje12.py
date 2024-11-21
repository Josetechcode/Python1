# DISPLAY PROGRAM TITLE
print ("*** PROGRAMA RESTA AL PRIMER NÚMERO EL SEGUNDO, SIEMPRE Y CUANDO EL PRIMERO SEA MAYOR ***")

num1 = int(input("ingresar el primer número: "))
num2 = int(input("ingresar el segundo número: "))

if num1 > num2:
  print ("El resultado de restarle al primer número al segundo es ",num1-num2)
else:
  print ("No es posible realizar la operación ya que el segundo número es mayor que el primero")