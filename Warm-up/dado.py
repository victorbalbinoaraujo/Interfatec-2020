qtd = int(input())
valor1 = 0
valor2 = 0
control = 0
for i in range(qtd):
    if control == 0:
        luisa = int(input())
        valor1 += luisa
        control = 1
        if luisa == 6:
            control = 0
    elif control == 1:
        antonio = int(input())
        valor2 += antonio
        control = 0
        if antonio == 6:
            control = 1

if valor1 > valor2:
    print(f'LUISA {valor1}')
elif valor2 > valor1:
    print(f'ANTONIO {valor2}')
else:
    print(f'EMPATE {valor1}')
    