a = input("")
b = "" #Первое число
h = 0
g = "" #Второе число
for i in range(len(a)):
    if a[i] != "+":
        b+= a[i]
    elif a[i] == "+" or "*" or "/" or "-":
        c = a[i]
        break
    h += 1
for i in range(h-len(a)+1,0):
    g += a[i]
b = int(b)
g = int(g)
if c == "-":
    print(b-g)
if c == "*":
    print(b*g) 
if c == "/":
    print(b/g)
if c == "+":
    print(b+g)