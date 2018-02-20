from Pelicula import *
from pila import *

def main():
    pilaPeliculasAccion = Pila()
    pelicula1 = Pelicula("El señor de los anillos","Elijah Wood", "Accion")
    pelicula2 = Pelicula("El origen","Leonardo Dicaprio", "Accion")
    pelicula3 = Pelicula("Matrix","Keanu Reeves", "Accion")
    pelicula4 = Pelicula("Gladiador","Russell Crowe", "Accion")
    pilaPeliculasAccion.apilar(pelicula1)
    pilaPeliculasAccion.apilar(pelicula2)
    pilaPeliculasAccion.apilar(pelicula3)
    pilaPeliculasAccion.apilar(pelicula4)
    print("1) Nombre de la película")
    print("2) Actor")
    print("3) Género")
    print("Ingrese alguna de las opciones para buscar")
    opt = input()
    if (opt == "1"):
        print("ingrese el nombre de la pelicula:")
        nombreP = input()
        while pilaPeliculasAccion.es_vacia() == False:
            obj = pilaPeliculasAccion.desapilar()
            if nombreP==obj.nombre:
                print("Nombre: " + obj.nombre + "\n  Actor: " + obj.actor + "\n  genero: " + obj.genero)

    elif opt == "2":
        print("ingrese el nombre del actor:")
        nombreActor = input()
        while pilaPeliculasAccion.es_vacia() == False:
            obj = pilaPeliculasAccion.desapilar()
            if nombreActor==obj.actor:

                print("Nombre: " + obj.nombre + "\n  Actor: " + obj.actor + "\n  genero: " + obj.genero)
    elif opt == "3":
        print("ingrese el genero de la pelicula")
        genero = input()
        while pilaPeliculasAccion.es_vacia() == False:
            obj = pilaPeliculasAccion.desapilar()
            if genero==obj.genero:
                print("Nombre: " + obj.nombre + "\n  Actor: " + obj.actor + "\n  genero: " + obj.genero)


if __name__ == "__main__":
    main()
