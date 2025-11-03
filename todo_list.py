# todo_list.py
tasks = []  # Сюда будем сохранять задачи

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Добавить задачу")
    print("2. Показать все")
    print("3. Удалить задачу")
    print("4. Выйти")
    return input("Выбери (1-4): ")

def add_task():
    task = input("Что нужно сделать? ")
    tasks.append(task)
    print(f"Задача добавлена: {task}")

def show_tasks():
    if not tasks:
        print("Список пуст!")
    else:
        print("\nТвои задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    show_tasks()
    if tasks:
        try:
            num = int(input("Номер задачи для удаления: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Удалено: {removed}")
            else:
                print("Неверный номер!")
        except:
            print("Введи число!")

# === ОСНОВНОЙ ЦИКЛ ===
while True:
    choice = show_menu()
    
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Пока! Ты продуктивен.")
        break
    else:
        print("Неверный выбор!")
    
    input("\nНажми Enter...")