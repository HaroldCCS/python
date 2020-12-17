import random

def run():
    adivina = random.randint(1, 100)

    encontrado = True
    preguntar = 0
    print('Ingresa un numero mayor a 0: ')
    while adivina == preguntar:
        if adivina > preguntar:
            preguntar = int(input('Ingresa un numero mayor: '))
        else:
            preguntar = int(input('Ingresa un numero menor: '))

    print('Excelente, Encontraste el numero!! es ' + str(adivina))


if __name__ == '__main__':
    run()