
n1=int(input("Ingrese el primer numero "))
n2=int(input("Ingrese el segundo numero "))
n3=int(input("Ingrese el tercer numero "))

if n1>n2 and n1>n3 and n2>n3:
    print("El orden es ",n1,n2,n3)
elif n1>n2 and n1>n3 and n3>n2:
    print("El orden es ",n1,n3,n2)
elif n2>n1 and n2>n3 and n1>n3:
    print("El orden es ",n2,n1,n3)
elif n2>n1 and n2>n3 and n3>n1:
    print("El orden es ",n2,n3,n1)
elif n3>n1 and n3>n2 and n1>n2:
    print("El orden es ",n3,n1,n2)
else:
    print("El orden es ",n3,n2,n1)