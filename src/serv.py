import os
import time
import sys
import platform

def cls():
    system = platform.uname()[0]
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")

def run_logo():
    try:
        os.system("python src/logo.py")
    except Exception as e:
        print(f"Ошибка при запуске логотипа: {e}")

def start_services():
    try:
        print("Запуск необходимых сервисов...")
        os.system("python src/Starter.py")
        time.sleep(2)
        print("Сервисы запущены.")
    except Exception as e:
        print(f"Ошибка при запуске сервисов: {e}")

def start():
    cls()
    start_services()
    cls()
    run_logo()

if __name__ == "__main__":
    start()