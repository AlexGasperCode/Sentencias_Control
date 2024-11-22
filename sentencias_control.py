# Ejercicio número 1
numero = int(input("Ingresa un número: "))
if 0 <= numero < 50:
    if numero > 25:
        print("Es mayor a 25")
    else:
        print("En menor a 25")
else:
    print("El número está fuera del rango")

# Ejercicio número 2
nota1 = int(input("Ingrese primer nota: "))
nota2 = int(input("Ingrese segunda nota: "))
nota3 = int(input("Ingrese tercer nota: "))
promedio = (nota1+nota2+nota3)/3
if promedio >= 8:
    print("Aprobado")
else:
    if promedio >= 4:
        print("Recuperación")
    else:
        print("Reprobado")

# Ejercicio número 3
for i in range(1,5):
    for e in range(1,10):
        print(i,e)

# Ejercicio número 4
numero = input('Introduce un número: ')
numero = int(numero)

if numero % 3 == 0:
    if numero % 5 == 0:
        print('El número', numero, 'es divisible por 3 y por 5')
    else:
        print('El número', numero, 'es divisible por 3')

# Ejercicio número 5
numero = 2 
while numero < 10 :  
    if numero % 2 == 0:  
        print("El número "+str(numero)+" es par")
    else:
        print("El número "+str(numero)+" es impar")
    numero = numero + 1