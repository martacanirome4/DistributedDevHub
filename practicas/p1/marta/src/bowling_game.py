# File: bowling_game.py
class PartidaBolos:

    def __init__(self):
        self.puntuacion = 0
        # usamos una lista de tuplas para representar los pares de puntuación de las rondas
        self.rondas = []

    def agregar_set(self, puntos_set):
        if len(puntos_set) != 2:
            raise ValueError("Cada ronda necesita dos sets de puntuación.")
        
        self.rondas.append(puntos_set)
        self.puntuacion = self.puntuacion + sum(puntos_set)

    def get_rondas(self):
        return self.rondas
    
    def get_puntuacion(self):
        return self.puntuacion


if __name__ == "__main__":
    partida = PartidaBolos()
    partida.agregar_set((5, 3))
    partida.agregar_set((7, 2))

    print("Puntuación:", partida.get_puntuacion())

    print("Rondas juego:", partida.get_rondas())