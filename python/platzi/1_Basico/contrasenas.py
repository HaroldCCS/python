import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'g']
    simbolos = ['!', '@', '%', '&', '$']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()
