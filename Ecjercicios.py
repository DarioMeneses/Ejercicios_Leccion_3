""" Escribir una clase en python llamada circulo, que contenga un radio,
    con un metodo que devuelva y otro el perimetro del circulo"""
    
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

# Objeto creado de la clase Circulo
mi_circulo = Circulo(5)  

# Calculo de área y  perímetro
area = mi_circulo.area()
perimetro = mi_circulo.perimetro()

# Imprimir los resultados
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

""" Escribir una clase en python con 2 metodos: get_string y print_string,
    el primero acepta una cadena de texto ingresada por el usuario y el 
    segundo imprime esa misma cadena en mayusculas """
    
class Cadena:
    def __init__(self):
        self.texto = ""

    def get_string(self):
        self.texto = input("Ingresa tu texto aqui: ")

    def print_string(self):
        print(self.texto.upper())

# Objeto creado de la clase Cadena
mi_cadena = Cadena()

# Texto obtenido del usuario
mi_cadena.get_string()

# Imprime la cadena en mayúsculas
mi_cadena.print_string()

