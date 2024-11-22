# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE VERIFICA 3 NOTAS Y CLASIFICA LOS RESULTADOS*** ")

Note_list = []

# PROMPT THE USER THE NUMBER OF NOTES
Nota1 = int (input("Ingresar la primera nota [1-100]: "))
Note_list.append(Nota1)
Nota2 = int (input("Ingresar la primera nota [1-100]: "))
Note_list.append(Nota2)
Nota3 = int (input("Ingresar la segunda nota [1-100]: "))
Note_list.append(Nota3)

print(Note_list)

if Nota1 > Nota2 and Nota1 > Nota3:
  print(f"(La nota {Nota1} fue la nota más alta")
  if Nota2 > Nota3:
    print(f"La nota {Nota3} fue la nota más baja")
  else:
    print(f"La nota {Nota2} fue la nota más baja")

elif Nota2 > Nota1 and Nota2 > Nota3:
  print(f"La nota {Nota2} fue la nota más alta")
  if Nota1 > Nota3:
    print(f"La nota {Nota3} fue la nota más baja")
  else:
    print(f"La nota {Nota1} fue la nota más baja")

elif Nota3 > Nota1 and Nota3 > Nota2:
  print(f"La nota {Nota3} fue la nota más alta")
  if Nota1 > Nota2:
    print(f"La nota {Nota2} fue la nota más baja")
  else:
    print(f"La nota {Nota1} fue la nota más baja")



print("La nota 100 fue obtenida por",Note_list.count(100), "estudiantes.")