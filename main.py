a = input("")
b = ""
h = 0
g = ""
for i in range(len(a)):
    if a[i] != "+":
        b+= a[i]

    elif a[i] == "+":
        break
    h += 1
for i in range(h-len(a),-1,-1):
    print(a[i])
print(b)