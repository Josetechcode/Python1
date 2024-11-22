# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE IDENTIFICA VOCALES*** ")

Letter = (input("Ingresar una letra: ")).capitalize()

if len(Letter) > 1:
  print("No puedo procesar el dato")
else:
  if Letter == 'A' or Letter == 'E' or Letter == 'I' or Letter == 'O' or Letter == 'U':
    print("Es vocal.")
  else:
    print("No es una vocal")