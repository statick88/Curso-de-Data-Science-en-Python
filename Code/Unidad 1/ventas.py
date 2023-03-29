import random
import csv

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
ventas = []
for dia in dias:
    venta = random.randint(1000, 5000)
    ventas.append({'Día': dia, 'Venta': venta})

with open('ventas.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Día', 'Venta'])
    writer.writeheader()
    for venta in ventas:
        writer.writerow(venta)

print("El archivo ventas.csv se ha generado con éxito.")