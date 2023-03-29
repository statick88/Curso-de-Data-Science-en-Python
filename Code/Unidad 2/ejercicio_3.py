from datetime import datetime

date_format = "%d/%m/%Y"

birth_date_str = input("Introduce tu fecha de nacimiento en formato dd/mm/yyyy: ")

birth_date = datetime.strptime(birth_date_str, date_format)
current_date = datetime.now()

age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

print(f"Tienes {age} años.")
