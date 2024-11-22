# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE INFORMA CALIFICACIÓN DE ACUERDO A RANGOS ESTABLECIDOS ***")

Nota = 11
# PROMPTING THE USER
while Nota < 0 or Nota > 10:
    Nota = float (input("Ingresar un valor válido [0 - 10]: "))

# CHECKING THE ENTERED GRADE AND DISPLAYING THE LITERAL GRADE
if Nota >= 9.1:
    print("La calificación literal es EXCELENTE!")
elif Nota >= 8.1:
    print("La calificación literal es MUY BIEN!")
elif Nota >= 7.5:
    print("La calificación literal es BIEN!")
else:
    print("La calificación literal es NO APROBADO!")