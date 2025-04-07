# #Actividad 1
edad1 = int(input("Ingrese su edad: "))

if edad1 >= 18:
    print("Es mayor de edad")

#Actividad 2
nota1 = int(input("Ingrese Nota: "))
if nota1 >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Actividad 3
numeroPar = int(input("Ingrese numero par: "))
if numeroPar % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Actividad 4
edad2 = int(input("Ingrese su edad: "))
if edad2 > 0 and edad2 < 12:
    print("Niño/a: menor de 12 años")
elif edad2 >= 12 and edad2 < 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años")
elif edad2 >= 18 and edad2 < 30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años")
elif edad2 >= 30:
    print("Adulto/a: mayor o igual que 30 años.")
else:
    print("valor no valido...")

#Actividad 5
contraseña = input("Ingrese contraseña entre 8 y 14 caracteres: ")
if 8 <= len(contraseña) <=14:
   print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6
import random
from statistics import mode, median, mean

#mi_lista = [1,2,5,5,3]
#print(mean(mi_lista))

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)

moda_aleatoria = mode(numeros_aleatorios)
mediana_aleatoria= median(numeros_aleatorios)
media_aleatoria = mean(numeros_aleatorios)

if media_aleatoria > mediana_aleatoria and mediana_aleatoria > moda_aleatoria:
    print("Sesgo positivo o a la derecha")
elif media_aleatoria < mediana_aleatoria and mediana_aleatoria < moda_aleatoria:
    print("Sesgo negativo o a la izquierda")
else: 
    print("Sin sesgo")

#Actividad 7
frase1 = input("Ingrese frase o palabra: ")
vocales = "aeiouAEIOU"

if frase1 and frase1[-1] in vocales:
    print(frase1,"!")
else:
    print(frase1)

#Actividad 8
nombre8 = input("Ingrese su nombre: ")
numero8 = int(input("Ingrese un Numero del 1,2,3: "))

if numero8 == 1:
    print(nombre8.upper())
elif numero8 == 2:
    print(nombre8.lower())
elif numero8 == 3:
    print(nombre8.title())
else:
    print("Numero invalido")

#Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print( "Menor que 3: Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Mayor o igual que 3 y menor que 4: Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Mayor o igual que 4 y menor que 5: Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Mayor o igual que 5 y menor que 6: Fuerte" )
elif magnitud >= 6 and magnitud < 7:
    print(" Mayor o igual que 6 y menor que 7: Muy Fuerte")
elif magnitud >= 7:
    print( "Mayor o igual que 7: Extremo")
else:
    print("Magnitud Invalida")

#Actividad 10
hemisferio = input("N/S: ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el dia (1-31): "))

if hemisferio == "N":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("Invierno")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("Primavera")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("Verano")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        print("Otoño")
    else:
        print("Fuera de Rango...")
elif hemisferio == "S":
     if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("Verano")
     elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("Otoño")
     elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("Invierno")
     elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        print("Primavera")
     else:
        print("Fuera de Rango...")
else:
    print("Hemisferio no valido")
