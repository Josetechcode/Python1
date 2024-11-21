# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE DETERMINA SI UN NÚMERO ES POSITIVO Y MAYOR QUE 100 ***")

# PROMPTING THE USER THE NUMBER TO VERIFY
num = int(input("Favor ingresar número q verificar: "))

# CHECKING THE NUMBER
if num > 0:
  # DISPLAY RESULT
  print("El número ingresado es positivo.")
  if num < 100:
    # DISPLAY RESULT
    print("El número ingresado es menor que 100.")
  else :
    # DISPLAY RESULT
    print("El número ingresado no es menor que 100.")
else :
  # DISPLAY RESULT
  print("El número ingresado es negativo.")