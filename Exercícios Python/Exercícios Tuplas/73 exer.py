print('\nExercicio 72')
print('Campeonato brasileiro\n')

t = ('Flamengo', 'Atlético', 'São Paulo', 'Internacional', 'Grêmio', 'Palmeiras', 'Sport Recife', 'Cruzeiro', 'Botafogo','Corinthians', 'Vasco', 'Fluminence', 'América', 'Chapecoense', 'Santos', 'Vitória', 'Bahia', 'Paraná', 'Atletico', 'Ceará')


print('Os cinco primeiros:', t[0:5])
print('-='*36)
print('Os cinco ultimos:', t[-5:])
print('-='*36)
print('Em ordem alfabética:', sorted(t))
print('-='*36)
print(f'O Chapecoense está em ', (t.index('Chapecoense'))+1, '° posição')
print('-='*36)

input()
