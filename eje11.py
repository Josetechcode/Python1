# DISPLAY PROGRAM TITLE
print ("*** PROGRAMA QUE SOLICITA NOMBRE, APELLIDO, EDAD Y NOTA PROMEDIO DE 5 ESTUDIANTES ***")

i = 0
List_notas = []

while i < 3:
  i += 1
  Nombre = (input("Ingresar nombre y apellido del estudiante: "))
  Edad = int(input("Ingresar edad del estudiante: "))
  Nota = float(input("Ingresar nota promedio del estudiante: "))
  
  List_notas.append(Nota)

Promedio = sum(List_notas)/3

print(f"El promedio de las notas {Promedio}.")