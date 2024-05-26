import unittest
from kata import Partida
class TestBolos(unittest.TestCase):
                  
  def test_exixte_partida(self):
    jugada= [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    partida= Partida()
    esperado = partida.tabla_partida
    self.assertEqual(jugada, esperado)

  def test_no_exixte_partida(self):
    jugada= [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    partida= Partida()
    resultado = partida.tabla_partida
    self.assertNotEqual(jugada, resultado)
  
  def test_lanzar_bolos(self):
    partida = Partida()
    tirada = partida.lanzar_bolos()
    self.assertLessEqual(sum(tirada), 10)
    
    
  def test_strike(self): 
    partida = Partida()
    jugada_strike =  [[0,0],[0,0],[0,0],[0,0],[10],[0,0],[0,0],[0,0],[0,0],[0,0]]
    partida.tabla_partida  =  jugada_strike 
    turno = partida.tabla_partida[4]
    self.assertTrue(turno)
    
  def test_spare(self): 
    partida = Partida()
    jugada_strike =  [[0,0],[0,0],[0,0],[0,0],[8,2],[0,0],[0,0],[0,0],[0,0],[0,0]]
    partida.tabla_partida  =  jugada_strike 
    turno = partida.tabla_partida[4]
    self.assertTrue(turno)
    

  def test_tirar_strike_ultima_ronda_mal(self): 
      partida = Partida()
      jugada_strike =  [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[5,2,8]]
      partida.tabla_partida = jugada_strike
      turno = partida.tabla_partida[9]
      self.assertNotEqual(turno[0], 10)
      
  def test_tirar_strike_ultima_ronda(self): 
      partida = Partida()
      jugada_strike =  [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[10,2,8]]
      partida.tabla_partida = jugada_strike
      turno = partida.tabla_partida[9]
      self.assertTrue(turno[0] == 10)
      
  def test_suma(self):
      partida=Partida()
      partida.tabla_partida=  [[0,0],[0,0],[0,0],[5,4],[1,2],[0,0],[0,0],[0,0],[0,0],[0,0]]
      suma_esperada=12
      total_puntos =partida.suma_puntos()
      self.assertEquals(suma_esperada,total_puntos)
  def test_suma_strike(self):
      partida=Partida()
      partida.tabla_partida=  [[0,0],[0,0],[0,0],[10],[1,2],[0,0],[0,0],[0,0],[0,0],[0,0]]
      suma_esperada=16
      total_puntos =partida.suma_puntos()
      self.assertEquals(suma_esperada,total_puntos)
      self.assertEquals(suma_esperada,total_puntos)
  
  def test_bonus_final_strike(self):
      partida = Partida()
      partida.tabla_partida = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[10,8,2]]
      puntos_esperados = 30
      puntos_obtenidos = partida.suma_puntos()
      self.assertEqual(puntos_esperados, puntos_obtenidos)
  def test_bonus_final_spare(self):
      partida = Partida()
      partida.tabla_partida = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[8,2,10]]
      puntos_esperados = 30
      puntos_obtenidos = partida.suma_puntos()
      self.assertEqual(puntos_esperados, puntos_obtenidos)


if __name__ == '__main__':
  unittest.main()