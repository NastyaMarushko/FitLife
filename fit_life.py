# Собираем информацию: имя, возраст, вес, рост
user_name = input("Добро пожаловать! Как Вас зовут? ")
user_name = user_name.title()

while True:
    user_age = input("Сколько Вам полных лет? ")
    try:
        int_user_age = int(user_age)
        break
    except ValueError:
        print("Пожалуйста, введите корректное целое число для возраста.")


while True:
    user_weight = input("Укажите свой вес в кг, используя точку (Пример: 68.7): ")
    try:
        float_user_weight = float(user_weight)
        break
    except ValueError:
        print("Пожалуйста, введите корректный вес (число с точкой, например, 71.3).")

while True:
    user_height = input("Укажите свой рост в метрах, используя точку (Пример: 1.77): ")
    try:
        float_user_height = float(user_height)
        if float_user_height <= 0:
            print("Рост должен быть положительным числом.")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите корректный рост (число с точкой, например, 1.69).")

# Подсчет ИМТ:
bmi = float_user_weight / (float_user_height**2)
round_bmi = round(bmi, 1)

# Подсчет воды:
water_per_kg_ml = 30
water_per_kg_l = water_per_kg_ml / 1000
water_needed = float_user_weight * water_per_kg_l
round_water_needed = round(water_needed, 1)

# Вывод  результата:
print("=" * 62)
print(f"Привет, {user_name}!")
print()
print(f"Твой полный возраст: {int_user_age}")
print(f"Твой вес(в кг.): {float_user_weight}")
print(f"Твой рост(в м.): {float_user_height}")
print("-" * 62)
print(f"На основе этих показателей твой ИМТ равен: {round_bmi}")
print(f"Твоя норма воды в день: {round_water_needed} л.")
print()
print("Расчет окончен. Будьте здоровы!")
