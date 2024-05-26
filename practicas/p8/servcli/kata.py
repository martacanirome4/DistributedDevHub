# p8/servcli/kata.py

class Kata:

    def esPalindromo(self, cadena):
        # Esta función devuelve True si la cadena es un palíndromo
        cadena = cadena.lower()
        return cadena == cadena[::-1]

    def esVocal(self, cadena):
        # Esta función devuelve el número de vocales en una cadena
        vocales = "aeiouAEIOU"
        return sum(1 for char in cadena if char in vocales)

    def startsWithA(self, cadena):
        # Esta función devuelve True si la cadena empieza por 'a'
        return cadena.lower().startswith('a')

    def palabrasConVocalesImpares(self, cadena):
        # Esta función devuelve la cadena si tiene un número impar de vocales
        return cadena if self.esVocal(cadena) % 2 == 1 else False

    def palabrasQueTenganTamañoMayorQue7(self, cadena):
        # Esta función devuelve la cadena si su tamaño es mayor o igual a 7
        return cadena if len(cadena) >= 7 else False

    def eliminarVocalesDeUnaCadena(self, cadena):
        # Esta función elimina las vocales de una cadena
        vocales = "aeiouAEIOU"
        return ''.join(char for char in cadena if char not in vocales)

    def annadirZDespuesDeUnaA(self, cadena):
        # Esta función añade una 'z' después de una 'a'
        return cadena.replace('a', 'az').replace('A', 'Az')

    def annadirXTresPosicionesMasDeUnaJ(self, cadena):
        # Esta función añade una 'x' tres posiciones después de una 'j'
        idx = cadena.lower().find('j')
        if idx != -1 and idx + 3 < len(cadena):
            return cadena[:idx + 3] + 'x' + cadena[idx + 3:]
        return cadena

    def entero_a_romano(self, numero):
        # Esta función convierte un número entero en un número romano
        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        resultado = ''
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado
