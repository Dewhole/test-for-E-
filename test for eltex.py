import string
import random
N = int(input("Введите длину строки "))
stringg = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(N))
print(stringg)

NN = str(input("Введите символ "))

for i in stringg:
    #Буквы не хаотичны, это порядок раскладки на клавиатуре
    if i == "P" or i == "O" or i == "I" or i == "U" or i == "Y" or i == "T" or i == "R" or i == "E" or i == "W" or i == "Q" or i == "L" or i == "K" or i == "J" or i == "H" or i == "G" or i == "F" or i == "D" or i == "S" or i == "A" or i == "M" or i == "N" or i == "B" or i == "V" or i == "C" or i == "X" or i == "Z":
        print(NN, end='')
    else:
        print(i, end='')

NNN = str(input("\nВведите еще один символ "))

    # ниже переменные для подсчёта количства символов
first = 0
second = 0

for i in stringg:
    #Буквы не хаотичны, это порядок раскладки на клавиатуре
    if i == "P" or i == "O" or i == "I" or i == "U" or i == "Y" or i == "T" or i == "R" or i == "E" or i == "W" or i == "Q" or i == "L" or i == "K" or i == "J" or i == "H" or i == "G" or i == "F" or i == "D" or i == "S" or i == "A" or i == "M" or i == "N" or i == "B" or i == "V" or i == "C" or i == "X" or i == "Z":
        print(NN, end='')
        first += 1
    else:
        print(NNN, end='')
        second += 1
print("\nКоличество символов", NN, "=", first)
print("Количество символов", NNN, "=", second)

input("\nВведите любой символ для завершения программы ")
