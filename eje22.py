# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE VERIFICA CANTIDAD DE CURSOS COMPRADOS Y APLICA DESCUENTOS*** ")

# PROMPT AMOUNT OF PURCHASED COURSES
Num = int (input("¿Cuántos cursos compró?: "))

if Num < 6:
    print("El valor a pagar por cada curso es $ 2'000,000.00 COP.\nEl pago total es: $",Num * 2000000,"COP.")
else:
    print("El valor a pagar por cada curso es $ 1'200,000.00 COP.\nEl pago total es: $",Num * 1200000,"COP.")