# calculator_v2.py
def show_menu():
    print("=== КАЛЬКУЛЯТОР v2 ===")
    print("1. Сложить")
    print("2. Вычесть")
    print("3. Умножить")
    print("4. Поделить")
    print("5. Выйти")
    return input("Выбери (1-5): ")

def get_numbers():
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    return a, b

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

# === ОСНОВНОЙ ЦИКЛ ===
while True:
    choice = show_menu()
    
    if choice == '5':
        print("Пока! Ты крут.")
        break
    
    if choice in ['1', '2', '3', '4']:
        num1, num2 = get_numbers()
        
        if choice == '1':
            print("Результат:", add(num1, num2))
        elif choice == '2':
            print("Результат:", subtract(num1, num2))
        elif choice == '3':
            print("Результат:", multiply(num1, num2))
        elif choice == '4':
            print("Результат:", divide(num1, num2))
    else:
        print("Неверный выбор! Попробуй снова.")
    
    input("\nНажми Enter для продолжения...")