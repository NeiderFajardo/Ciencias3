from pila import *
from arbol import *

class Compilador:
    def __init__(self):
        #Guarda la variable incognita
        self.variable=""
        self.errorSimbolo=0
        self.errorNumero=0
        #Operacion a realizar
        self.lista=[]
        #Pila para ordenar el arbol
        self.pilaNodos=Pila()

    #Verifica que no hay nada después del igual, que antes del igual vaya una variable
    def verificar(self, sentencia):
        if sentencia[len(sentencia)-1]=="=":
            sentencia.pop()
            if sentencia != [] and sentencia[len(sentencia)-1].isalpha():
                self.variable = sentencia.pop()
                if sentencia != [] and sentencia[len(sentencia)-1] in "+-/*":
                    return True
        return False

    def convertir(self, lista, pila,cuentaNumeros):
        if lista != []:
            if lista[0] in "+-*/=":
                if pila.es_vacia() != True:
                    nodo_der = pila.desapilar()
                else:
                    return False
                if pila.es_vacia() != True:
                    nodo_izq = pila.desapilar()
                else:
                    return False
                pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
                cuentaNumeros=0
            else:
                if cuentaNumeros<2:
                    pila.apilar(Nodo(lista[0]))
                    cuentaNumeros=cuentaNumeros+1
                else:
                    return False
            return self.convertir(lista[1:],pila,cuentaNumeros)
        return True

    def evaluar(self, arbol):
        if arbol.valor == "+":
            return self.evaluar(arbol.izq) + self.evaluar(arbol.der)
        if arbol.valor == "-":
            return self.evaluar(arbol.izq) - self.evaluar(arbol.der)
        if arbol.valor == "/":
            return self.evaluar(arbol.izq) / self.evaluar(arbol.der)
        if arbol.valor == "*":
            return self.evaluar(arbol.izq) * self.evaluar(arbol.der)
        return int(arbol.valor)

    def ejecutar(self, lista):
        self.lista = lista
        if (self.verificar(lista) == False):
            print("Error")
        else:
            if self.convertir(lista, self.pilaNodos,self.errorNumero) == False:
                print("Error")
            else:
                print (self.variable+" = "+str(self.evaluar(self.pilaNodos.desapilar())))
