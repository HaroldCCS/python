def primo(numero):
    razon = True
    for i in numero:
        if i % 2 != 0:
            razon = False
            break
    return razon


def run():
    numero = int(input('Ingrese un numero: '))

    if primo(numero):
      print('El numero es primo')
    else:
      print('El numero NO es primo')


if __name__ == '__main__':
    run()
