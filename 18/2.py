'''Около Васиного компьютера сидит вредный попугай. 
Он бьет клювом по клавише со знаком равенства (=). 
Посчитай, сколько раз попугай ударил по клавише.'''

a = input()
k=0

for c in a:
    if c == "=":
        k +=1
print(k)