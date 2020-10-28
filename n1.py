import os

filename = input("Введите путь к файлу, путь не должен быть длиннее 6 символов: ")

if os.path.exists(filename) and len(filename) <= 6:
    print("файл существует")
else:
    print("файл не существует")
