#Задание 3
a ="А роза упала на лапу Азора"
c = ""
b = a.replace(" ","")
g = b.lower()
for i in range(len(a)-1, -1, -1):
    c += a[i]
t = c.replace(" ","")
f = t.lower()
if g == f:
    print("Да")
else:
    print("Нет")
