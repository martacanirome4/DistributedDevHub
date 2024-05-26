# p9/KataRomanos.py

class KataRomanos:
    def entero_a_romano(self, numero):
        valores = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        resultado = ''
        for valor, simbolo in valores.items():
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado

    def romano_a_entero(self, romano):
        valores = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        resultado = 0
        for i in range(len(romano)):
            if i > 0 and valores[romano[i]] > valores[romano[i-1]]:
                resultado += valores[romano[i]] - 2 * valores[romano[i-1]]
            else:
                resultado += valores[romano[i]]
        return resultado

    def es_numero_romano(self, romano):
        simbolos_romanos = ["I", "V", "X", "L", "C", "D", "M"]
        for caracter in romano:
            if caracter not in simbolos_romanos:
                return False
        return True
