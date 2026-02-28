#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
problemas.py
------------

Tarea sobre búsquedas, donde lo que es importante es crear nuevas heurísticas

"""

import busquedas



# ------------------------------------------------------------
#  Desarrolla el modelo del Camión mágico
# ------------------------------------------------------------

class PbCamionMagico(busquedas.ProblemaBusqueda):
    """
    ---------------------------------------------------------------------------------
     Supongamos que quiero trasladarme desde la posición discreta $1$ hasta 
     la posicion discreta $N$ en una vía recta usando un camión mágico. 
    
     Puedo trasladarme de dos maneras:
      1. A pie, desde el punto $x$ hasta el punto $x + 1$ en un tiempo de 1 minuto.
      2. Usando un camión mágico, desde el punto $x$ hasta el punto $2x$ con un tiempo 
         de 2 minutos.

     Desarrollar la clase del modelo del camión mágico
    ----------------------------------------------------------------------------------
    
    """
    def __init__(self):
        pass

    def acciones(self, estado):
        posicion, meta = estado
        acciones = []
        if posicion <= meta:
            acciones.append("un paso")

        if posicion * 2 <= meta:
            acciones.append("camion magico")

        return acciones

    def sucesor(self, estado, accion):
        posicion, meta = estado
        if accion == 'un paso':
            estado_sucesor = (posicion + 1, meta)
            costo_local = 1
        elif accion == 'camion magico':
            estado_sucesor = (posicion * 2, meta)
            costo_local = 2

        return estado_sucesor, costo_local

    def terminal(self, estado):
        posicion, meta = estado
        return posicion == meta

    @staticmethod
    def bonito(estado):
        """
        El prettyprint de un estado dado

        """
        posicion, meta = estado
        return print(f"Posicion: {posicion} Meta: {meta}")
 

# ------------------------------------------------------------
#  Desarrolla una política admisible.
# ------------------------------------------------------------

def h_1_camion_magico(nodo):
    """
    Esta heuristica asume un escenario extremadamente optimista, lo que seria un
    problema relajado, simplemente calcula cuantas veces tendriamos que usar el camion magico
    para alcanzar o rebasar la meta, pero imaginando que el camión cuesta solo 1 minuto
    en lugar de 2. Es admisible porque al aplicar este descuento, garantizamos
    matematicamente que la estimacion siempre sera menor o igual al tiempo real
    que tomaria llegar. Es decir, nunca va a sobrestimar el costo.

    """
    estado_actual, meta = nodo.estado
    saltos = 0

    while estado_actual < meta:
        estado_actual *= 2
        saltos += 1

    return saltos

# ------------------------------------------------------------
#  Desarrolla otra política admisible.
#  Analiza y di porque piensas que es (o no es) dominante una
#  respecto otra política
# ------------------------------------------------------------

def h_2_camion_magico(nodo):
    """
    Como esta heuristica trabaja desde la meta hasta el estado inicial y no
    al reves, no es cuestion de "atinarle" a que movimiento hacer, en cualquier
    momento sabe si usar camion magico (si divisible entre 2) o solo dar
    un paso (cuando no es divisible entre 2).

    """
    estado_actual, meta = nodo.estado
    actual = meta
    costo_estimado = 0

    while actual > estado_actual:
        if actual % 2 == 0 and (actual // 2) >= estado_actual:
            actual = actual // 2
            costo_estimado += 2
        else:
            actual -= 1
            costo_estimado += 1

    return costo_estimado

# ------------------------------------------------------------
#  Desarrolla el modelo del cubo de Rubik
# ------------------------------------------------------------

class PbCuboRubik(busquedas.ProblemaBusqueda):
    """
    La clase para el modelo de cubo de rubik, documentación, no olvides poner
    la documentación de forma clara y concisa.
    
    https://en.wikipedia.org/wiki/Rubik%27s_Cube
    
    """
    def __init__(self):
        raise NotImplementedError('Hay que hacerlo de tarea')

    def acciones(self, estado):
        raise NotImplementedError('Hay que hacerlo de tarea')

    def sucesor(self, estado, accion):
        raise NotImplementedError('Hay que hacerlo de tarea')

    def terminal(self, estado):
        raise NotImplementedError('Hay que hacerlo de tarea')

    @staticmethod
    def bonito(estado):
        """
        El prettyprint de un estado dado

        """
        raise NotImplementedError('Hay que hacerlo de tarea')
 

# ------------------------------------------------------------
#  Desarrolla una política admisible.
# ------------------------------------------------------------
def h_1_problema_1(nodo):
    """
    DOCUMENTA LA HEURÍSTICA QUE DESARROLLES Y DA UNA JUSTIFICACIÓN
    PLATICADA DE PORQUÉ CREES QUE LA HEURÍSTICA ES ADMISIBLE

    """
    return 0


# ------------------------------------------------------------
#  Desarrolla otra política admisible.
#  Analiza y di porque piensas que es (o no es) dominante una
#  respecto otra política
# ------------------------------------------------------------
def h_2_problema_1(nodo):
    """
    DOCUMENTA LA HEURÍSTICA DE DESARROLLES Y DA UNA JUSTIFICACIÓN
    PLATICADA DE PORQUÉ CREES QUE LA HEURÍSTICA ES ADMISIBLE

    """
    return 0



def compara_metodos(problema, pos_inicial, heuristica_1, heuristica_2):
    """
    Compara en un cuadro lo nodos expandidos y el costo de la solución
    de varios métodos de búsqueda

    @param problema: Un objeto del tipo ProblemaBusqueda
    @param pos_inicial: Una tupla con una posicion inicial
    @param heuristica_1: Una función de heurística
    @param heuristica_2: Una función de heurística

    """
    solucion1, nodo1 = busquedas.busqueda_A_estrella(problema, pos_inicial, heuristica_1)
    solucion2, nodo2 = busquedas.busqueda_A_estrella(problema, pos_inicial, heuristica_2)
    
    print('-' * 50)
    print('Método'.center(12) + 'Costo'.center(18) + 'Nodos visitados'.center(20))
    print('-' * 50 + '\n')
    print('A* con h1'.center(12) 
          + str(solucion1.costo).center(18) 
          + str(nodo1))
    print('A* con h2'.center(12) 
          + str(solucion2.costo).center(20) 
          + str(nodo2))
    print('-' * 50 + '\n')


if __name__ == "__main__":

    # Compara los métodos de búsqueda para el problema del camión mágico
    # con las heurísticas que desarrollaste
    print("\n" + "=" * 50)
    print("=== RESOLVIENDO EL CAMION MAGICO ===")
    pos_inicial = (1, 50)  # <--- PONLE LA POSICIÓN INICIAL QUE QUIERAS
    problema = PbCamionMagico()  # <--- PONLE LOS PARÁMETROS QUE NECESITES
    compara_metodos(problema, pos_inicial, h_1_camion_magico, h_2_camion_magico)
    
    # Compara los métodos de búsqueda para el problema del cubo de rubik
    # con las heurísticas que desarrollaste
    #pos_inicial = XXXXXXXXXX  # <--- PONLE LA POSICIÓN INICIAL QUE QUIERAS
    #problema = PbCuboRubik( XXXXXXXXXX )  # <--- PONLE LOS PARÁMETROS QUE NECESITES
    #compara_metodos(problema, h_1_problema_1, h_2_problema_1)
    