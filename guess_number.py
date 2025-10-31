import random  # Для случайных чисел

# Бот загадывает число от 1 до 10
secret_number = random.randint(1, 10)
attempts = 0  # Счётчик попыток

print("Игра: Угадай число! Я загадал от 1 до 10.")
print("Подсказки: 'Меньше' / 'Больше' / 'Угадал!'")

# Цикл while — играем, пока не угадаем
while True:  # Бесконечный цикл, break прервёт
    guess = int(input("Твоё число: "))  # Ввод от юзера
    attempts += 1  # +1 попытка
    
    if guess < secret_number:
        print("Слишком мало! Попробуй больше.")
    elif guess > secret_number:
        print("Слишком много! Попробуй меньше.")
    else:
        print(f"УГАДАЛ! За {attempts} попыток. Загаданное: {secret_number}")
        break  # Выход из цикла

print("Игра окончена. Ты крут!")