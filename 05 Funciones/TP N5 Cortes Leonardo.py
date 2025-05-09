### Práctico 5: Listas
### Cortes Leonaro Nahuel
# Actividades 1
lista1_100 = []

for num in range(1,101):
    if num % 4 == 0:
        lista1_100.append(num)

print(lista1_100)

# Actividad 2

gusten = [3.14 , 22, 1984, False, "UTN"]

print(gusten[-2])

# Actividad 3
lista_vacia = []

lista_vacia.append("uno")
lista_vacia.append("dos")
lista_vacia.append("tres")

print(lista_vacia)

# Actividad 4
animales = ["perro", "gato", "conejo", "pez"]

animales[2] = "loro"
animales[-1] = "oso"

print(animales)

# Actividad 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#Este progrma define una lista de numeros y elimina 
# el numero mas alto de esa lista en este caso el 22
# luego muestra la lista por pantalla.

# Actividad 6
lista10_30 = []
for num2 in range(10,31,5):
    lista10_30.append(num2)

print(lista10_30[0:2])

# Actividad 7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "Focus"
autos[2] = "Vento"

print(autos)

# Actividad 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

# Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#Agrega "jugo" a la lista del tercer cliente con append
compras[2].append("jugo") 
#Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines" 
#Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
#Imprimir la lista resultante por pantalla
print(compras)

# Actividad 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
 
print(lista_anidada)
