# #Actividad 1
for cont in range(101):
    print(cont)

# #Actidiad 2
num1 = int(input("Ingrese un Numero: "))
num1 = abs(num1)
contador = 0

if num1 == 0:
    contador = 1
else:
    var1 = num1
    while var1 > 0:
        var1 = var1 // 10
        contador += 1

print(f"El numero {num1} tiene {contador} digitos.")

# #Actividad 3
Valor1 = int(input("Ingrese Primer Numero: "))
Valor2 = int(input("Ingrese Segundo Numero: "))
suma_val = 0

if Valor1 < Valor2:
    for num in range(Valor1+1, Valor2):
        suma_val += num
elif Valor2 < Valor1:
    for num in range(Valor2+1, Valor1):
        suma_val += num

print("La suma de los numeros entre los dos valores es = ", suma_val)

# #Actividad 4
num2 = 1
sumando = 0

while num2 != 0:
    num2 = int(input("Ingrese un Numero a sumar: "))
    sumando = sumando + num2

print(f"Total acumulado es = {sumando}")

# Actividad 5
from random import *
aleatorio = randint(0,9)
print(aleatorio)
print("Juego donde el usuario adivina el numero aleatorio...")
conta = 0
ficha = -1
while aleatorio != ficha:
    ficha = int(input("Ingrese Numero:"))
    conta += 1
if conta == 1:
    print("Ganaste el 1er Puesto capo....")
else:
    print("Adivinasten en el intento numero: ",conta," Segui Participando...")

# Actividad 6
for i in range(101,0,-1):
    if i % 2 == 0:
        print(i)

#Actividad 7
entero_positivo = int(input("Ingrese un numero entero positivo: "))
contadorSuma = 0
for z in range(0,entero_positivo+1):
    contadorSuma = contadorSuma + z
    print(contadorSuma)
print("La suma total de la cuaneta es: ",contadorSuma)

# Actividad 8
contar_Par = 0 
contar_Impar = 0 
negativo = 0 
positivo = 0
for y in range(100):
    num_usuario = int(input("ingrese numero: "))
    if num_usuario % 2 == 0:
        contar_Par += 1
    else:
        contar_Impar += 1
    
    if num_usuario > 0:
        positivo += 1
    elif num_usuario < 0:
        negativo +=1

print("tOTAL DE numeros pares: ",contar_Par)
print("tOTAL DE numeros Impares: ",contar_Impar)
print("tOTAL DE numeros Positivos: ",positivo)
print("tOTAL DE numeros Negativos: ",negativo)

# Actividad 9
numeros_media = 0
media = 0
for t in range(100):
    numeros_media = int(input("Ingrese Numeros: "))
    media = media + numeros_media
media = media/100
print("Media = ",media)

# Actividad 10
numero_original = int(input("Ingrese numero: "))
numero_Invertido=0
bandera=0
original= numero_original
if numero_original < 0:
    numero_original=numero_original * -1
    bandera += 1


while numero_original > 0:
    digito = numero_original % 10
    numero_Invertido = (numero_Invertido*10) + digito
    numero_original //= 10

if bandera == 1:
    numero_Invertido = numero_Invertido * -1

print(f"El numero original es: {original}")
print(f"El numero Invertido es:{numero_Invertido}")
