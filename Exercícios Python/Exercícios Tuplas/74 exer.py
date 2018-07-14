from random import randint

a = randint(0,999999)
b = randint(0,999999)
c = randint(0,999999)
d = randint(0,999999)
e = randint(0,999999)

t = (a, b, c, d, e)

print(f'A lista é {t}')
print(f'O maior número é o {sorted(t)[0]}')
print(f'O menor número é {sorted(t)[-1]}')

input()
