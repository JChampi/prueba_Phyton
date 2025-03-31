"string"
'string'

"""hla que tal 
    aqui se puede hacer
    varios saltos con comillas dobles"""
    
'''hola aqui tambien se puede 
    realiar saltos con 
    comillas simples '''

#Con esto se puede realizar comentarios en las lineas de codigo
#----------------------------------------------

nro = 2
nombre = "jos"
edad = 20
color = "azul"

# Concatenar con f strings
pantalla = f"Hola {nombre} tu edad es: {edad} y tu color es : {color}"
print(pantalla)

#Concatenar con +
print("Mensaje -->" + pantalla)

# Operadores de pertenencia = (in /  in not)
print("hoho" in pantalla)

#---------------------------------------------

# Datos compuestos
lista = ["jos", "mturin", 20, "nation"] # un arreglo se puede modificar
#posicion [0]         [1]     [2]    [3]
lista[0] = "Marito"
print(lista[0])

tupla = ("jos", "mturin", 20, "nation") # una tupla no se puede modificar
#tupla[0] = "Marito"   ---> va salir error
print(tupla[0])
#Pero se puede mdificar toda la tupla :
tupla = ("jfdksflkdslfkds")
print(tupla)

#----------------------------------------------------- 

# Creando un Conjunto (set) 
conjunto = {"jos", "mturin", True, 21,"jps"}
print(conjunto) # Elimina los elementos duplicados
                # print(conjunto[0]) --> Ademas no se accede por posicion o indice

#-----------------------------------------------------------------

# Diccionario (dict)
diccionario = {    
    'nombre' : " Jos ",    
    'edad ' : 20,
    'esta_feliz' : True,
    'tiene clases': True
} 

print(diccionario["nombre"])





