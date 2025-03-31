# PROGRAMA PARA CALCULAR EL PROMEDIO FINAL
C1 = float(input("Ingrese el C1: "))
parcial = float(input("Ingrese el Parcial: "))
C2 = float(input("Ingrese el C2: "))
final = float(input("Ingrese la nota final: "))

promedio = (C1*0.20) + (parcial*0.20) + (C2*0.20) + (final*0.40) 

print(f"El promedio es: ", promedio)