import random

class Partida():
    def __init__ (self): 
        self.tabla_partida =[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.ronda_actual = 0
        
    def lanzar_bolos(self):
        tirada= []
        tirada.append(random.randint(0,10))
        tirada.append(random.randint(0,10 - tirada[0]))
        return tirada 
    
    def tirar_strike(self, turno):
        return turno[0] == 10
    def tirar_spare(self, turno):
        return sum(turno) == 10 and turno[0] != 10
    def suma_puntos(self):
        puntos_totales = 0
        strike_acumulado = False
        spare_acumulado = False
        for i, ronda in enumerate(self.tabla_partida):
            if strike_acumulado:
                puntos_totales += 2 * sum(ronda)
                strike_acumulado = False
            elif spare_acumulado:
                puntos_totales += puntos_totales +  ronda[0] + ronda[1]
            else:
                puntos_totales += sum(ronda)
            
            if self.tirar_strike(ronda):
                strike_acumulado = True
            elif self.tirar_spare(ronda):
                spare_acumulado = True
                

    
        return puntos_totales

    
                    
        