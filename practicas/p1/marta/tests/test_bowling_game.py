# Test file for the BowlingGame class
import unittest
from src.bowling_game import PartidaBolos

class TestPartidaBolos(unittest.TestCase):
    
    # open frame (ronda abierta): el jugador no tira los diez bolos, se anota el número de bolos que tire en la ronda
    def test_open_frame(self):

        partida = PartidaBolos()

        partida.agregar_set((5, 3))

        self.assertEqual(8, partida.get_puntuacion())

    def test_open_frame_a_medias(self):

        partida = PartidaBolos()

        with self.assertRaises(ValueError):
            partida.agregar_set((5,))


    def test_open_frame_demasiados_puntos(self):

        partida = PartidaBolos()

        with self.assertRaises(ValueError):
            partida.agregar_set((5, 3, 2))


    # strike: el jugador tira 10 bolos en primer intento, se anota diez bolos más el número de bolos que tire en sus siguientes dos bolas
    def test_strike(self):

        partida = PartidaBolos()
        
        pass


    # spare: el jugador tira 10 bolos entre los dos intentos, se anota diez bolos más el número de bolos que tire en su siguiente bola
    def test_pasar_ronda(self):
        partida = PartidaBolos()
        pass


if __name__ == '__main__':
    unittest.main()
