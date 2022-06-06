"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
"""

while True:
    num_1 = int(input('Digite um número entre 0 e 10: '))
    if num_1 > 10:
        print('Apenas números entre 0 e 10!!! ')
    elif 0 <= num_1 <= 10:
        print(f'Valor válido!\n'
              f'Você digitou o número: {num_1}')
        break

print('Fim do programa!!! ')