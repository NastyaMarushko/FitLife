WATER_PER_KG_ML = 30
WATER_ML_PER_L = 1000
SEPARATING_LINE_ONE = "-" * 62
SEPARATING_LINE_TWO = "=" * 62

# Собираем информацию: имя, возраст, вес, рост
user_name = input("Добро пожаловать! Как Вас зовут? ")
user_name = user_name.title()

while True:
    user_age = input("Сколько Вам полных лет? ")
    try:
        int_user_age = int(user_age)
        break
    except ValueError:
        print("Пожалуйста, введите целое число")


while True:
    user_weight = input("Укажите свой вес в кг (69.9) ")
    try:
        float_user_weight = float(user_weight)
        if float_user_weight < 0:
            print("Обратите внимание - вес не может быть отрицательным")
            continue
        break
    except ValueError:
        print("Используйте точку. Пример: 71.3")

while True:
    user_height = input("Укажите свой рост в метрах (1.77): ")
    try:
        float_user_height = float(user_height)
        if float_user_height <= 0:
            print("Рост должен быть положительным числом")
            continue
        break
    except ValueError:
        print("Введите число с точкой (прим. 1.69)")

# Подсчет ИМТ:
bmi = float_user_weight / (float_user_height**2)
round_bmi = round(bmi, 1)

# Подсчет воды:
water_per_kg_l = WATER_PER_KG_ML / WATER_ML_PER_L
water_needed = float_user_weight * water_per_kg_l
round_water_needed = round(water_needed, 1)

# Вывод  результата:
print(SEPARATING_LINE_TWO)
print(f"Привет, {user_name}!")
print()
print(f"Твой полный возраст: {int_user_age}")
print(f"Твой вес(в кг.): {float_user_weight}")
print(f"Твой рост(в м.): {float_user_height}")
print(SEPARATING_LINE_ONE)
print(f"На основе этих показателей твой ИМТ равен: {round_bmi}")
print(f"Твоя норма воды в день: {round_water_needed}")
print()
print("Расчет окончен. Будьте здоровы!")
