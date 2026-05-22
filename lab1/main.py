current_year = 2026

name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
birth_year = int(input("Введите год рождения: "))
height = float(input("Введите ваш рост (см): "))

age = current_year - birth_year

print("****************************************")
print("*          ВАША ВИЗИТКА               *")
print("****************************************")
print(f"* Имя: {name}")
print(f"* Фамилия: {surname}")
print(f"* Год рождения: {birth_year}")
print(f"* Возраст: {age} года")
print(f"* Рост: {height} см")
print("****************************************")