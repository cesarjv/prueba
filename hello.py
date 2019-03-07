def suma(num1,num2):   # Funciones. Funciona siempre con parametro por referencia
    num3=num1+num2
    return num3

def evaluacion(nota):

    if nota<5:
        valorado="Reprobado"
    else:   
        valorado="Aprobado"       
    return valorado    

res=suma(1,2)   # Guardando el valor que retorna la funcion despues de ejecutarse
print(res)  

miLista=["Maria",2,12.03,"Pepe"]
print(miLista[:])

miLista.append("cesar")  # Agregando elemento
print(miLista[:])

miLista.remove("Maria")  # Eliminado Elemento
print(miLista[:])

miLista.insert(2,"Carlos")   # Insertando Elemento en una posicion especifica
print(miLista[:])

print(miLista.index(2))    # Identificando La posicion de cierto elemento dentro de la lista
print (2 in miLista)       # Comprobar si un elemento esta en una lista

#Tupla  Guarda ciertas similitudes con las lista, pero difieren en muchas caracteristicas, de las principales es que no se pueden modificar

tupla1=("Juan","Marcos",2,3.5,"Estaban")   
print(tupla1[:])

miLista1=list(tupla1)  # Convierto la tupla en lista
print(miLista1[:])

mitupla=tuple(miLista)  # Convierto la lista en tupla
print(mitupla[:])

print(mitupla.count(12.03))  # Contando cuantos elementos hay de ese valor dentro de la tupla/lista

print(len(mitupla))  # contando cuantos elementos en total hay dentro de la tupla/lista

mitupla1=("Juan",26,"Feb",1995)
nom,dia,mes,ano=mitupla1                # Desempaquetando una tupla en variables
print(nom)

# Diccionarios   son tipo de un array asociativo con la caracteristica de valor:clave

my_diccionario={"Alemania":"Berlin","España":"Madrid","Venezuela":"Caracas","Argentina":"Buenos Aires"}
print(my_diccionario["Alemania"])
print(my_diccionario)

my_diccionario["Italia"]="Roma"   # Agregando un nuevo elemento al diccionario
print(my_diccionario) 
del my_diccionario["Venezuela"]  # Eliminando un valor del array asociativo o diccionario
print(my_diccionario)

print(my_diccionario.keys())   # Imprimiendo las claves 

print(my_diccionario.values())  # Imprimiendo los valores

print(len(my_diccionario))

a = 10
 
if(a <= 5):
    print("a es menor o igual que 5")
else:
    print("a es mayor que 5")

print(evaluacion(10))
