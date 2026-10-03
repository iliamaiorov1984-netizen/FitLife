# Проект FitLife - MVP версия 1.0

def get_age_ending(age):
    """Функция для определения правильного склонения возраста"""
    if age in range(1, 122, 10) and age not in (11, 111):
        return ' год'
    elif str(age)[-1] in ('234') and age not in range(12, 15) and age < 110:
        return ' года'
    else:
        return ' лет'


def is_correct(user_data, word):
    """Функция для проверки корректности ввода"""
    try:
        res = float(user_data) if word in ('вес', 'рост') else int(user_data)
        if res < 0:
            word_title = word.title()
            print(f'Ошибка ввода!\n{word_title} '
                  f'должен быть положительным числом. Попробуйте снова.\n')
            return is_correct(input(f'Укажите свой {word}: '), word)
        return res
    except ValueError:
        word_title = word.title()
        if word == 'возраст':
            print(f'Ошибка ввода!\n{word_title} '
                  f'должен быть целым числом. Попробуйте снова.\n')
        else:
            print(f'Ошибка ввода!\n{word_title} '
                  f'должен быть целым или дробным числом с точкой '
                  f'в качестве разделителя. Попробуйте снова.\n')
        return is_correct(input(f'Укажите свой {word}: '), word)


# 1. Знакомство
print('\nПривет! Я Ваш фитнес-бот.\n'
      'Я умею рассчитывать индекс массы тела '
      'и могу дать рекомендации по потреблению воды.\n')


# 2. Сбор данных
user_name = input('Давайте знакомиться. '
                  'Как я могу к Вам обращаться?\nВведите имя: ')
print(f'Очень приятно, {user_name}!\n')

user_age = is_correct(input('Укажите свой возраст: '), 'возраст')
user_age = str(user_age) + get_age_ending(user_age)
user_weight = is_correct(input('Укажите свой вес в килограммах: '), 'вес')
user_height = is_correct(input('Укажите свой рост в метрах: '), 'рост')


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_l = (user_weight * 30) / 1000

# 4. Вывод красивого результата
print(f'\n\nОтчет для пользователя {user_name}. '
      f'Возраст {user_age}\nиндекс массы тела равен - {bmi}\n'
      f'рекомендуемая суточная норма потребления воды '
      f'- {water_l} л\n\nРасчёт окончен. Будьте здоровы!')
