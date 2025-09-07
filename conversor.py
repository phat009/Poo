calif=int(input("Ingrese la calificacion: "))

if calif in range(90,101):
    print("La calificación es A")
elif calif in range(80,90):
    print("La calificación es B")
elif calif in range(70,80):
    print("La calificación es C")
elif calif in range(60,70):
    print("La calificación es D")
else:
    print("La calificación es F")