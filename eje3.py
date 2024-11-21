# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE INDICA NÚMERO MAYOR, MENOR O SI HAY NUMEROS IGUALES ENTRE TRES NÚMEROS INGRESADOS ***")

# PROMPTING THE USER THE NUMBER TO VERIFY
num1 = int(input("Favor ingresar el primer número: "))
num2 = int(input("Favor ingresar el segundo número: "))
num3 = int(input("Favor ingresar el tercer número: "))

# DETERMINING THE GREATEST NUMBER
if num1 > num2 and num1 > num3:
  if num2 > num3:
    # DISPLAY RESULT
    print("El numero mayor es el primer numero y el menor es el tercer número.")
  else:
    # DISPLAY RESULT
    print("El numero mayor es el primer numero y el menor es el segundo número.")

elif num2 > num1 and num2 > num3:
  if num3 > num1:
    # DISPLAY RESULT
    print("El numero mayor es el segundo numero y el menor es el primer número.")
  else:
    # DISPLAY RESULT
    print("El número mayor es el segundo número y el menor es el tercer número.")

elif num3 > num1 and num3 > num2:
  if num1 > num2:
    # DISPLAY RESULT
    print("El numero mayor es el tercer numero y el menor es el segundo número.")
  else:
    # DISPLAY RESULT
    print("El número mayor es el tercer número y el menor es el primer número.")

else:
  # DISPLAY RESULT
  if num1 == num2 and num1 == num3 and num2 == num3:
    # DISPLAY RESULT
    print("Todos los números ingresados son iguales.")
  elif num1 == num2:
    # DISPLAY RESULT
    print("El primer y segundo número son iguales.")
  elif num1 == num3:
    # DISPLAY RESULT
    print("El primero y tercer número son iguales")
  elif num2 == num3:
    # DISPLAY RESULT
    print("El segundo y tercer número son iguales")