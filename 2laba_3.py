#Задача 3

def leap_year(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return True

year = int(input("Введите номер года: "))

if leap_year(year) == True:
    print(year, "- високосный год.")
else:
    print(year, "- невисокосный год.")