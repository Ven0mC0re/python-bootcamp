# КАЛЬКУЛЯТОР (сохрани как calculator.py)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на 0!"
    return a / b

# Основная программа
print("Простой калькулятор")
print("1. Сложить")
print("2. Вычесть")
print("3. Умножить")
print("4. Поделить")

choice = input("Выбери (1-4): ")
num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))

if choice == '1':
    print("Результат:", add(num1, num2))
elif choice == '2':
    print("Результат:", subtract(num1, num2))
elif choice == '3':
    print("Результат:", multiply(num1, num2))
elif choice == '4':
    print("Результат:", divide(num1, num2))
else:
    print("Неверный выбор")