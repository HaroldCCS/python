def crearArchivo ():
    archivo=open('datos.txt' , 'w') #     w      es para  crear archivos
    archivo.close()

def modificar():
    archivo=open('datos.txt' , 'a') #       a       es para modificar un archivo
    archivo.write ('Mi nombre es Harold Camargo  \n')      #     \n para salto de linea
    archivo.write ('tengo 18 años')
    archivo.close()

def lectura():
        archivo=open('datos.txt' , 'r') #       r       es para leer un archivo
        linea=archivo.readline()
        while linea!="":
            print (linea)
            linea=archivo.readline()
        archivo.close()



        
#crearArchivo()
#modificar()
lectura()
