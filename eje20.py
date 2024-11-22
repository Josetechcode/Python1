# DISPLAYING PROGRAM TITLE
print ("*** PROGRAMA QUE VERIFICA SI PUEDES FORMAR PARTE DEL EQUIPO DE BASKETBALL*** ")

# PROMPT THE USER HOW OLD THEY ARE
Age = int(input("¿Cuántos años tienes?: "))

if Age <= 19:
    
    # PROMPT THE USER HOW TALL THEY ARE
    Height = float(input("¿Cuánto mides de estatura [cm]?: "))
    
    if Height >= 175:
        
        # PROMPT THE USER HOW MUCH THEY WEIGH
        Weight = float(input("¿Cuánto pesas [kg]?: "))
        
        if Weight >= 75 and Weight <= 80:

            # DISPLAYING APPLICATION RESULT
            print("¡Felicitaciones, puedes ser parte del equipo de basketball!")
        else:

            # DISPLAYING APPLICATION RESULT
            print("¡No puedes ser parte del equipo de basketball!")
    else:

        # DISPLAYING APPLICATION RESULT
        print("¡No puedes ser parte del equipo de basketball!")
else:

    # DISPLAYING APPLICATION RESULT
    print("¡No puedes ser parte del equipo de basketball!")