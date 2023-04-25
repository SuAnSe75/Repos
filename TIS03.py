'''
Ввод только цифры.
0 - досрочное окончание экзамена'''

import colorama 
from colorama import Fore, Back, Style

def cls(): 
    print("\n" * 2)
g = 0
cls()
print('"Раздатчик билетов version 1.13 SuAnSe"')
print('Введите количество билетов на экзамене: ')
n = int(input())
arr = [0] * n
for t in range (n):
    arr[t] = t + 1
cls()
print(arr)
print("Выберите № билета:      (0 - конец экзамена)")
b = int(input())
while b != 0:

    if 0 < b <= n:
        if arr[b-1] == '_':
            cls()
            print(Fore.RED + "Билет использован! Повторите ввод!")
            g = g - 1 
        arr[b-1] = '_'
     
        if arr.count('_') == n:
            g = g + 1
            cls()
            print(Fore.RED + "Билеты кончились!")
            break   
        g = g + 1
        cls()
        print(Style.RESET_ALL)
        print(arr)
        print("Выберите № следующего билета:      (0 - конец экзамена)")
        b = int(input())

    else:
        cls()
        print(Fore.RED + "Такого билета нет! Повторите ввод!")
        cls()
        print(Style.RESET_ALL)
        print(arr)
        print("Выберите № следующего билета: ")
        b = int(input())
cls()
print(Style.RESET_ALL)
print(Back.BLUE + f"Билетов взято {g} шт. Осталось {n - g} шт. Экзамен закончен!")
print(Style.RESET_ALL)