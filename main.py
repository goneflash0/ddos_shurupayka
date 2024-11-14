import os
import time
from pystyle import Colors, Colorate

# Цвета для вывода текста
color_code = {
    "reset": "\033[0m",
    "dark": "\033[38;5;240m"
}

# Очистка экрана перед запуском
os.system("clear")

# Меню
menu = """
┌───────────────────────────────────────────────┐
│            [1] DDoS по IP адресу              │
├───────────────────────────────────────────────┤
│            [2] Получить IP адрес по URL       │
├───────────────────────────────────────────────┤
│            [3] Логи DDoS атак                 │
└───────────────────────────────────────────────┘
"""

centered_menu = "\n".join([line.center(110) for line in menu.split("\n")])
colored_menu = Colorate.Vertical(Colors.white_to_black, centered_menu)
print(colored_menu)

# Выбор действия
try:
    op = int(input(f'{color_code["dark"]}[✿] Выберите действие => {color_code["reset"]}'))

    if op == 1:
        # Запрос на ввод IP-адреса и порта
        target_ip = input("Введите IP адрес для атаки: ")
        target_port = int(input("Введите порт для атаки: "))

        # Передаем IP и порт как аргументы в ddos.py
        os.system(f"python3 src/ddos.py {target_ip} {target_port}")

    elif op == 2:
        # Выполнение скрипта для получения IP по URL
        os.system("python3 src/Url.py")

    elif op == 3:
        # Открытие логов DDoS атак
        os.system("python3 src/log-ddos.py")

    else:
        print("\033[1;31;40mНеверный ввод. Перезагружаю инструменты!")
        time.sleep(1.6)
        os.system("python3 main.py")  # Перезапуск main.py при неверном вводе

except ValueError:
    print("\033[1;31;40mНеверный ввод. Пожалуйста, введите номер действия.")
    time.sleep(1.6)
    os.system("python3 main.py")
