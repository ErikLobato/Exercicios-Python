a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))

t = (a, b, c, d)

print(f'\nOs valores digitados foram {t}')

if 9 in t:
    print(f'O 9 apareceu {t.count(9)} vezes')
else:
    print('O 9 não aparece')

if 3 in t:
    print(f'O primeiro 3 está na {(t.index(3))+1}° posição')
else:
    print('O 3 não aparece na lista')

p = 0    
for c in range(0,4):
    if t[c] % 2 == 0:
        print(f'{t[c]} ', end='')
        p += 1
if p == 1:
    print(' é o número par')
elif p > 1:
    print('são os números pares')
else:
    print('Não tem números pares')

input()
