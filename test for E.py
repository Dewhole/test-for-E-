import string
import random
N = int(input("Введите длину строки "))
stringg = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(N))
print(stringg)

NN = str(input("Введите символ "))

for i in stringg:
    if i.isalpha:
        print(NN, end='')
    else:
        print(i, end='')

NNN = str(input("\nВведите еще один символ "))

    # ниже переменные для подсчёта количства символов
first = 0
second = 0

for i in stringg:
    if i.isalpha:
        print(NN, end='')
        first += 1
    else:
        print(NNN, end='')
        second += 1
print("\nКоличество символов", NN, "=", first)
print("Количество символов", NNN, "=", second)

input("\nВведите любой символ для завершения программы ")
