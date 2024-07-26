# agrega libreria 
import math

# solicitar datos a usuario

Peso = float(input("Ingrese su peso en kg:\n>"))
Altura = float(input("Ingrese su altura en cm:\n>"))

# convertir cm a metros

Altura1 = Altura / 100

# Calculo IMC

IMC = Peso / math.pow(Altura1, 2)

# Mostrar Resultado IMC 

print(f"Su IMC es {round(IMC,2)}")

if IMC < 18.5 :
    print("Su Clasificacion segun OMS es BAJO PESO")

elif 18.5 <= IMC < 25 :
    print("Su clasificacion segun OMS es ADECUADO")

elif 25 <= IMC < 30 :
    print("Su clasificacion segun OMS es SOBREPESO")

elif 30 <= IMC < 35 :
    print("Su clasificacion segun OMS es OBESIDAD GRADO 1")

elif 35 <= IMC  < 40 :
    print("Su clasificacion segun OMS es OBESIDAD GRADO 2")

else :
    print("Su clasificacion segun OMS es OBESIDAD GRADO 3")