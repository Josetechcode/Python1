# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE INFORMA EL SIGNO ZODIACAL")

# PROMPTING THE USER THE MONTH
Mes = 13
while Mes < 1 or Mes > 12:

    Mes = int(input("Ingresar el mes de nacimiento [1 - 12]:\n1. Ene. 2. Feb. 3. Mar. 4. Abr. 5. May. 6. Jun.\n7. Jul. 8. Ago. 9. Sept. 10. Oct. 11. Nov. 12. Dic.\n"))
    print("")

# PROMPTING THE USER THE DAY OF THE MONTH
Dia = 0
while Dia < 1 or Dia > 31:
    Dia = int(input("Ingresar el dia de nacimiento [1 - 31]: "))
    print("")

# CHECKING JANUARY
if Mes == 1:
    if Dia >= 20:
        print("Su signo zodiacal es Acuario.")
    else:
        print("Su signo zodiacal es Capricornio.")

# CHECKING FEBRUARY
elif Mes == 2:
    if Dia >= 19:
        print("Su signo zodiacal es Piscis.")
    else:
        print("Su signo zodiacal es Acuario.")

# CHECKING MARCH
elif Mes == 3:
    if Dia >= 21:
        print("Su signo zodiacal es Aries.")
    else:
        print("Su signo zodiacal es Piscis.")

# CHECKING APRIL
elif Mes == 4:
    if Dia >= 20:
        print("Su signo zodiacal es Tauro.")
    else:
        print("Su signo zodiacal es Aries.")

# CHECKING MAY
elif Mes == 5:
    if Dia >= 21:
        print("Su signo zodiacal es Géminis.")
    else:
        print("Su signo zodiacal es Tauro.")

# CHECKING JUNE
elif Mes == 6:
    if Dia >= 21:
        print("Su signo zodiacal es Cáncer.")
    else:
        print("Su signo zodiacal es Géminis.")

# CHECKING JULY
elif Mes == 7:
    if Dia >= 23:
        print("Su signo zodiacal es Leo.")
    else:
        print("Su signo zodiacal es Cáncer.")

# CHECKING AUG
elif Mes == 8:
    if Dia >= 23:
        print("Su signo zodiacal es Virgo.")
    else:
        print("Su signo zodiacal es Leo.")

# CHECKING SEPT
elif Mes == 9:
    if Dia >= 23:
        print("Su signo zodiacal es Libra.")
    else:
        print("Su signo zodiacal es Virgo.")

# CHECKING OCT
elif Mes == 10:
    if Dia >= 23:
        print("Su signo zodiacal es Escorpio.")
    else:
        print("Su signo zodiacal es Libra.")

# CHECKING NOV
elif Mes == 11:
    if Dia >= 22:
        print("Su signo zodiacal es Sagitario.")
    else:
        print("Su signo zodiacal es Escorpio.")

# CHECKING DEC
elif Mes == 12:
    if Dia >= 22:
        print("Su signo zodiacal es Capricornio.")
    else:
        print("Su signo zodiacal es Sagitario.")