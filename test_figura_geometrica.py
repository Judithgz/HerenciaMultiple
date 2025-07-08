from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion Objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion Objecto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, 8, 'azul')
print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#MRO - Method Resolution Order
#print(Cuadrado.mro()) # Muestra como llaman las clases a sus metodos

#print(Rectangulo.mro()) # Muestra como llaman las clases a sus metodos