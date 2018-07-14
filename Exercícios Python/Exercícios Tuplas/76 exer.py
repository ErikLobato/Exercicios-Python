t = ('Frutas', 'R$:0,50', 'Suco', 'R$:2,50', 'PF', 'R$:12,50', 'Miojo', 'R$:0,99')
print(f'{t}\n')

for c in range(0,8):
    print(t[c], end=' ')
    if c % 2 != 0:
        print('\n', end='')

input()

