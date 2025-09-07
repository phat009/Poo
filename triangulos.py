
n1=int(input("Ingrese el primer lado: "))
n2=int(input("Ingrese el segundo lado: "))
n3=int(input("Ingrese el tercer lado: "))


if n1 == n2 and n2 == n3:
        print ("El triangulo es equilatero")
elif n1==n2 or n1==n3 or n2==n3:
        print("El triangulo es isósceles")
else :
        print("El triangulo es escaleno")