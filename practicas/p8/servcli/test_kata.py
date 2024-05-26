# p8/tests/test_kata.py

import pytest
from kata import Kata

p1 = Kata()

def test1():
    assert p1.esPalindromo("somos")

def test2():
    assert not p1.esPalindromo("noPalindromo")

def test3():
    assert p1.esVocal("hola") == 2

def test4():
    assert p1.esVocal("murcielago") == 5

def test5():
    assert p1.esPalindromo("ana")

def test6():
    assert hasattr(Kata, "esPalindromo")

def test7():
    assert hasattr(Kata, "esVocal")

def test8():
    assert p1.startsWithA("Amanda")

def test9():
    assert not p1.startsWithA("tuyaaya")

def test10():
    assert p1.startsWithA("ana")

def test11():
    assert p1.palabrasConVocalesImpares("maria") == "maria"

def test12():
    assert not p1.palabrasConVocalesImpares("raul")

def test13():
    assert p1.palabrasQueTenganTamañoMayorQue7("mamaguevo") == "mamaguevo"

def test14():
    assert not p1.palabrasQueTenganTamañoMayorQue7("d3")

def test15():
    assert p1.eliminarVocalesDeUnaCadena("keloke") == "klk"

def test16():
    assert p1.eliminarVocalesDeUnaCadena("klk") == "klk"

def test17():
    assert p1.annadirZDespuesDeUnaA("Alocado") == "Azlocazdo"

def test18():
    assert p1.annadirZDespuesDeUnaA("orco") == "orco"

def test19():
    assert p1.annadirXTresPosicionesMasDeUnaJ("joder") == "jodxer"

def test20():
    assert p1.annadirXTresPosicionesMasDeUnaJ("olla") == "olla"

def test21():
    assert p1.entero_a_romano(2021) == "MMXXI"

def test22():
    assert p1.entero_a_romano(1094) == "MXCIV"

def test23():
    assert p1.entero_a_romano(47) == "XLVII"
