'''17 задача 18
Даня составляет кроссворд. Слова с четным количеством
 букв он располагает горизонтально, а с нечетными -
  вертикально.
Дано слово. Если в нем четное количество букв,
 вывели все буквы в строку через пробел, иначе -
  в столбик через пробел.'''

a = input()
if len(a) % 2 == 0:
    for c in a:
        print(c, end=" ")
elif len(a) % 2 == 1:
    for c in a:
        print(c)