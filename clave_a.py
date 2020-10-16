import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma(numero1, numero2):
    return numero1 + numero2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares():
    contador = 0
    suma = 0
    while contador <= 500:
        suma = suma + contador * 2
        contador = contador + 1
    result = suma
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro(radio, altura):
    result = float(2 * radio * altura * 3.14159 + 2 * radio * radio * 3.14159)
    result = round(result, 2)
    return result


def areaLateral(radio, altura):
    result = float(2 * radio * altura * 3.14159)
    result = redondear(result, 2)
    return result


def areaCirculo(radio, altura):
    result = float(2 * radio * radio * 3.14159)
    result = redondear(result, 2)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def areaTotalCilindro(self):
        result = float(
            2 * self.radio * self.altura * 3.14159
            + 2 * self.radio * self.radio * 3.14159
        )
        result = round(result, 2)
        return result


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    def __init__(self):
        self.listaPedidos = []

    def ordenar(self, nombre, lugar, costo, conDescuento, descuento):
        pizza = Pizza(nombre, lugar, costo, conDescuento, descuento)
        self.listaPedidos.append(pizza)

    def costoTotal(self):
        costoTotal = 0
        for pizza in self.listaPedidos:
            costo = pizza.getCosto()
            costoTotal = costoTotal + costo
            costoTotal = round(costoTotal, 2)
            costoTotalDolares = f"${costoTotal}"
        return costoTotalDolares

    def costoTotalConDescuento(self):
        costoTotalConDescuentos = 0
        for pizza in self.listaPedidos:
            costoNormal = pizza.getCosto()
            descuento = pizza.getDescuento()
            costoTotalConDescuentos = costoTotalConDescuentos + (
                costoNormal - descuento
            )
            costoTotalConDescuentos = round(costoTotalConDescuentos, 2)
            costoTotalConDescuentosDolares = f"${costoTotalConDescuentos}"
        return costoTotalConDescuentosDolares


class Pizza:
    def __init__(self, nombre, lugar, costo, conDescuento, descuento):
        self.nombre = nombre
        self.lugar = lugar
        self.costo = costo
        self.conDescuento = conDescuento
        self.descuento = descuento

    def getNombre(self):
        return self.nombre

    def getLugar(self):
        return self.lugar

    def getCosto(self):
        return self.costo

    def getConDescuento(self):
        return self.conDescuento

    def getDescuento(self):
        return self.descuento


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""

# github url-->


def getGithubUrl():
    return ""
