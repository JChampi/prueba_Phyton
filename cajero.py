#Programa de un cajero automatico simple

saldo = 0
cant = 0

while True:
    
    print("""
    MENU DE OPCIONES
    1. INGRESAR
    2. RETIRAR
    3. MOSTRAR
    4. SALIR  
    """)
    
    op = int(input("Ingrese una opción: "))
    
    if op <= 0 or op > 4:
        print("Opción no válida. Ingresa una opción entre 1 y 4.")
        continue  
    
    # Si la opción es 4, salir del programa
    if op == 4:
        print("Saliendo del programa.")
        break

    # Proceso de ingreso de dinero
    if op == 1:
        cant = float(input("Ingrese la cantidad: "))
        if cant < 0:
            print("Error... ingresa valores positivos.")
        else: 
            saldo += cant
            print(f"Has ingresado {cant}. El saldo actual es: {saldo}.")
    
    # Proceso de retiro de dinero
    elif op == 2:
        cant = float(input("Ingrese la cantidad: "))
        if cant < 0:
            print("Error... ingresa valores positivos.")
        elif cant > saldo:
            print("Error... no tienes suficiente saldo para retirar esa cantidad.")
        else: 
            saldo -= cant
            print(f"Has retirado {cant}. El saldo actual es: {saldo}.")
    
    # Mostrar el saldo actual
    elif op == 3:    
        print(f"El saldo actual es: {saldo}")
    
    print("-----------------------------------------------------")


