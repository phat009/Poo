edad=int(input("Ingrese la edad del cliente: "))

if edad in range (0,13):
    print("Pague 50 pesos")
elif edad in range(13,17):
    print("Pague 80 pesos")
else:
    print("Pague 120 pesos")