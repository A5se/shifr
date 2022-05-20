from posixpath import join
import pyAesCrypt
import os

#Ф-ия шифрования
def encription(file,password):

    #Задаем размер буфера
    buffer_size = 512*1024

    #Вызываем метод щифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file)+".scr",
        password,
        buffer_size

    )
    print("[Файл '"+str(os.path.splitext(file)[0]) + "'зашифрован]")
    os.remove(file)
#Функция сканирования деректорий
def walking_by_dirs(dir,password):

    #перебираем все директории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        #Если находим файл шифруем
        if os.path.isfile(path):
            try:
                encription(path,password)
            except Exception as ex:
                print(ex)
        #если находим файл, то повторяем цикл в поиске файлов

        else:
            walking_by_dirs(path,password)
password = input("Введите пароль")
walking_by_dirs("D:\incoming\sesst", password)