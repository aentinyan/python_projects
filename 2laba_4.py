# Задача 4

first_color = input("Введите первый цвет (красный, синий или желтый): ")
second_color = input("Введите второй цвет (кроме того, что вы указали до этого): ")

if first_color not in ["красный", "синий", "желтый"] or second_color not in ["красный", "синий", "желтый"]:
    print("Ваш ответ невалиден.")
else:
    if first_color in ["красный", "синий"] and second_color in ["красный", "синий"]:
        print("Получившийся цвет - фиолетовый.")
    elif first_color in ["красный", "желтый"] and second_color in ["красный", "желтый"]:
        print("Получившийся цвет - оранжевый.")
    elif first_color in ["желтый", "синий"] and second_color in ["желтый", "синий"]:
        print("Получившийся цвет - зеленый.")