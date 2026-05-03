# Собираем информацию: имя, возраст, вес, рост
user_name = input("Добро пожаловать в FitLife! ")
user_name += input("Пожалуйста, введите своё имя: ")
user_name = user_name.title()

user_age = input("Сколько Вам полных лет? ")
int_user_age = int(user_age)

user_weight = input("Укажите свой ВЕС в кг, используя точку ")
user_weight += input("(Пример: 68.7) Ваш ответ: ")
float_user_weight = float(user_weight)

user_height = input("Укажите свой РОСТ в метрах, используя точку ")
user_height += input("(Пример: 1.77) Ваш ответ: ")
float_user_height = float(user_height)

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
print(f"На основе этих показателей твой ИМТ равен: {round_bmi} ")
print(f"Твоя норма воды в день: {round_water_needed} л. ")
print()
print("Расчет окончен. Будьте здоровы!")
