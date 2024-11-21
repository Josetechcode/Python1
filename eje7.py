# DISPLAY PROGRAM TITLE
print ("*** PROGRAMA QUE CALCULA COSTO TOTAL Y DESCUENTO (SI APLICA) ***")

check = float(input("INGRESAR EL VALOR DE LA CUENTA A PAGAR ($COP): "))

if check > 130000:
  print("EL VALOR A PAGAR ES ", check - check*0.15,"$COP.")
else:
  print("EL VALOR A PAGAR ES ",check,"$COP (DESCUENTO NO APLICABLE).")