# DISPLAY PROGRAM TITLE
print ("*** PROGRAMA QUE CALCULA EL VALOR TOTAL DE 5 PRODUCTOS, IVA, SUBTOTAL (ANTES DE IVA) Y TOTAL DESPUÉS DE IMPUESTOS ***")

i = 0
Productos = []

# PRODUCT COUNTER 
while i < 5:
  i += 1
  
  # PROMPTING THE VALUES
  Valor_unit = int(input("Ingresar costo del producto: "))

  # CREATING A VELUES LIST
  Productos.append(Valor_unit)

# ADDING THE VALUES UP
Sub_total = sum(Productos)

# CALCULATING IVA
Iva = Sub_total * 0.19

# CALCULATING THE COST AFTER TAXES
Total = Sub_total * (1.19)

# DISPLAYING THE IVA, COST BEFORE AND AFTER TAXES
print("")
print(f"A contiación se confirma los valores ingresados: {Productos}$COP.\nEl costo total de los productos antes de impuestos es: {Sub_total}$COP.\nPor concepto de IVA el valor a pagar es {Iva}$COP.\nEl valor despues de impuestos es: {Total}$COP.")