# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE VERIFICA SI PUEDES FORMAR PARTE DEL EQUIPO DE BASKETBALL*** ")

Num = int(input("¿Cuántos postulantes vas a ingresar?: "))

i = 0
j = 0
k = 0
l = 0
while i < Num:
    i += 1
    print(f"Ingresar el postulante número {i}")
    # PROMPT THE USER HOW OLD THEY ARE
    Age = int(input("¿Cuántos años tiene?: "))

    if Age <= 19:
        
        # PROMPT THE USER HOW TALL THEY ARE
        Height = float(input("¿Cuánto mide de estatura [cm]?: "))
        
        if Height >= 175:
            # APPLICANTS WHO PASSED TWO ASSESMENTS COUNTER
            j += 1
            # PROMPT THE USER HOW MUCH THEY WEIGH
            Weight = float(input("¿Cuánto pesa [kg]?: "))
            
            if Weight >= 75 and Weight <= 80:
                # APPLICANTS WHO WERE ACCEPTED IN THE TEAM COUNTER
                k += 1
                # DISPLAYING APPLICATION RESULT
                print("¡El postulante puede ser aceptado equipo de basketball!")
            else:
                # APPLICANTS WHO DIDN´T PASS ACCEPTED IN THE TEAM
                l += 1
                # DISPLAYING APPLICATION RESULT
                print("¡No puedes ser aceptado en el equipo de basketball!")
        else:
            # APPLICANTS WHO DIDN´T PASS ACCEPTED IN THE TEAM COUNTER
            l += 1
            # DISPLAYING APPLICATION RESULT
            print("¡No puedes ser aceptado en el equipo de basketball!")
    else:
        # APPLICANTS WHO DIDN´T PASS ACCEPTED IN THE TEAM COUNTER
        l += 1
        # DISPLAYING APPLICATION RESULT
        print("¡No puedes ser aceptado en el equipo de basketball!")

print(k," = entraron al equipo.\n",j," = pasaron dos requisitos de tres.\n",l," = no lograron entrar al equipo.")