from compilador2 import *

def cargarArchivo(nombre):
    archivo = open(nombre, "r")
    lista=[]
    for linea in archivo.readlines():
        lista.append(linea[:-2])
    return lista

def main():
    compilador=Compilador()
    expresiones=[x.split() for x in cargarArchivo("archivo.txt")]
    for i in range(len(expresiones)):
        compilador.ejecutar(expresiones[i])

if __name__ == "__main__":
    main()
