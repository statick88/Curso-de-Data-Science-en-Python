from datetime import datetime

date_format = "%d/%m/%Y"

date_str1 = input("Introduce una fecha en formato dd/mm/yyyy: ")
date_str2 = input("Introduce otra fecha en formato dd/mm/yyyy: ")

date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

days_diff = abs((date2 - date1).days)

print(f"La diferencia entre {date_str1} y {date_str2} es de {days_diff} días.")
