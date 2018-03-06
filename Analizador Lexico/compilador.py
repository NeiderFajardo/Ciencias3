from pila import *
from arbol import *

aux = 0
pila=Pila()
lista1 =[]

def cargarArchivo(nombre):
    archivo = open(nombre,"r")
    lista =[]
    for linea in archivo.readlines():
        lista.append(linea[:-1])
    return lista


def errorLexico(pos):
    lista1[pos-1]=">>"+lista1[pos-1]+"<<"
    print("Error en la siguiente posicion")
    print lista1
    exit()

def convertir(lista, pila, aux):
    aux=aux+1
    if lista != []:
        if lista[0] in "+-*/=":
            if pila.es_vacia() != True:
                nodo_der = pila.desapilar()
            else:
                errorLexico(aux)
            if pila.es_vacia() != True:
                nodo_izq = pila.desapilar()
            else:
                errorLexico(aux)
            #if pila.es_vacia() == False:
                #print pila.desapilar().valor
                #print lista[0]
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila,aux)

def evaluar(arbol):
    if arbol.valor == "=":
        resultado =arbol.der.valor+ "=" +str(evaluar(arbol.izq))
        return resultado
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)


var =(cargarArchivo("archivo.txt"))
lista1 = var[0].split()
def main():
    convertir(lista1, pila, aux)
    print (evaluar(pila.desapilar()))


if __name__ == "__main__":
    main()
