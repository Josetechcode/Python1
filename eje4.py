# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE CALCULA ÁREAS DE UN TRIÁNGULO O UN CÍRCULO ***")

# PROMT THE USER WHAT THEY WANT TO DO
choice = input("FAVOR INGRESAR UN VALOR VÁLIDO.\nT. CALCULAR ÁREA DE UN TRIÁNGULO.\nC. CALCULAR EL ÁRE DE UN CÍRCULO.\n").upper()

# CHECK THE USER´S CHOICE
if choice != 'T' and choice != 'C':
  # DISPLAY RESULT
  print("INGRESASTE UN OPCION NO VÁLIDA (T o C son opciones válidas).")
elif choice == 'T':
  Altura = int(input("INGRESAR ALTURA DEL TRIÁNGULO: "))
  Base = int(input("INGRESAR BASE DEL TRIÁNGULO: "))
  # DISPLAY RESULT
  print("EL ÁREA DEL TRIÁNGULO ES ",(Base * Altura)/2,".")
else:
  Radio = int(input("INGRESAR RADIO DEL CÍRCULO: "))
  # DISPLAY RESULT
  print("EL ÁREA DE LA CIRCUNFERENCIA ES ",3.1416 * Radio**2,".")