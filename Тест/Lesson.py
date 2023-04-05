import random
ma = 0
mi = 100
a = [""]*10
b = 0
while b < len(a):
    a[b] =  random.randint(0, 5)
    print(b, "--" , a[b])
    if a[b] > ma:
        ma = a[b]
    elif a[b] < mi:
        mi = a[b]
    b += 1
print(f'max: {ma}')   
print(f'min: {mi}')
x = a[0]
a[0] = a[9]
a[9] = x
print("меняем первую и последнюю")
print(f'Новое значение a[0]: {a[0]}')
print(f'Новое значение a[9]: {a[9]}')