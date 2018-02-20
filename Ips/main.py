# -*- coding: cp1252 -*-
from Paciente import *
from cola import *

cardiologia=Cola()
geriatria=Cola()
def organizarPaciente(paciente):
    if (paciente.especialidad=="cardiologia"):
        
        cardiologia.encolar(paciente)
    else:
        geriatria.encolar(paciente)
def mostrarCola(cola):
    if(cola.es_vacia()):
        return("")
    else:
        print(cola.desencolar().nombre)
        return mostrarCola(cola)

def main():
    paciente1 = Paciente("Gomez", "cardiologia")
    paciente2 = Paciente("Neider", "geriatria")
    paciente3 = Paciente("Cristian", "cardiologia")
    paciente4 = Paciente("Miguel", "cardiologia")
    paciente5 = Paciente("Eduardo", "geriatria")
    paciente6 = Paciente("Frederick", "cardiologia")
    paciente7 = Paciente("Paolo", "geriatria")
    paciente8 = Paciente("Wilo", "cardiologia")
    paciente9 = Paciente("Camila", "cardiologia")
    paciente10 = Paciente("Jose", "geriatria")
    print("añadiendo pacientes a las listas")
    organizarPaciente(paciente1)
    organizarPaciente(paciente2)
    organizarPaciente(paciente3)
    organizarPaciente(paciente4)
    organizarPaciente(paciente5)
    organizarPaciente(paciente6)
    organizarPaciente(paciente7)
    organizarPaciente(paciente8)
    organizarPaciente(paciente9)
    organizarPaciente(paciente10)
    print("Cola en espera de cardiologia")
    print(mostrarCola(cardiologia))
    print("Cola en espera de geriatria")
    print(mostrarCola(geriatria))

if __name__ == "__main__":
    main()
