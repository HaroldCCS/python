def run():
    poblacion_paises = {
        'Argentina': 2412121,
        'Brazil': 56345364,
        'Colombia': 455423
    }
    # trae indeices, argentina brazil
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # # trae valores
    # for pais in poblacion_paises.values():
    #     print(pais)

    # # trae indices y valores
    # for pais, poblacion in poblacion_paises.items():
    #     print(pais)
    #     print(poblacion)

    for pais in poblacion_paises.iteritems():
        print(pais)


if __name__ == '__main__':
    run()
