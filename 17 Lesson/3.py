'''
Аня называет число трекрасным, если оно делится на 3
 или если количество цифр в нем делится на три.
Дан номер билета, который Ане продали в трамвае. 
Проверь, трекрасно ли это число. Выведи Да или Нет.
'''
a = input()
if a != '':
    if (len(a) % 3 == 0) or (int(a) % 3 == 0):
        print("Да")
    else:
        print("Нет")
else:
    print("Вы не ввели цифры")