# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE INFORMA EL SALDO Y EL INTERÉS PAGADO AL FINAL DEL PERIODO ***")

# PROMPTING THE USER
Saldo = int (input("Ingresar el saldo al final del periodo [$COP]: "))
print("")

if Saldo < 100000:
    print(f"Con un saldo de {Saldo}$COP al final del periodo, se un generó un interés de ",Saldo * 0.03,"$COP [E.A.].")
else:
    print(f"Con un saldo de {Saldo}$COP al final del periodo, se un generó un interés de ",Saldo * 0.04,"$COP [E.A.].")