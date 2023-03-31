puntos = int(input("Ingrese la cantidad de puntos obtenidos en el examen: "))

if puntos >= 90:
    print("La calificación es A.")
elif puntos >= 80:
    print("La calificación es B.")
elif puntos >= 70:
    print("La calificación es C.")
elif puntos >= 60:
    print("La calificación es D.")
else:
    print("La calificación es F.")
