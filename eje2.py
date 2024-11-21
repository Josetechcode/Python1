# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE CALCULA EL MAYOR DE 3 NÚMEROS INGRESADOS ***")

# PROMPTING THE USER THE NUMBER TO VERIFY
num1 = int(input("Favor ingresar el primer número: "))
num2 = int(input("Favor ingresar el segundo número: "))
num3 = int(input("Favor ingresar el tercer número: "))

# DETERMINING THE GREATEST NUMBER
if num1 > num2 and num1 > num3 and num1 != num2 and num1 != num3:
  # DISPLAY RESULT
  print("El primer número ingresado es el mayor.")

elif num2 > num1 and num2 > num3 and num2 != num3 and num2 != num3:
  # DISPLAY RESULT
  print("El segundo número ingresado es el mayor.")

elif num3 > num1 and num3 > num2 and num3 != num1 and num3 != num2:
  # DISPLAY RESULT
  print("El tercer número ingresado es el mayor.")