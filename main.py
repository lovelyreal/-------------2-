from random import randint
h = 0
g = 0
u = 0

s=[]
for i in range (10):
    a = randint(-100,100)
    s.append(a)
    if a < 0:
        h+=1
    if a > 0:
        g += 1
    if a == 0:
        u += 1
print(h)
print(g)
print(u)
print(max(s),min(s))
print(s)