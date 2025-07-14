# Dependency inversion (Inversion de dependencias(SOLID)) 
from abc import ABC

"""
class Animal(ABC): # Esto es una interfaz
    def comer(self):
        print("Estoy comiendo")

    def caminar(self):
        print("Estoy caminando")
    
    def volar(self):
        print("Estoy volando")
    
    def nadar(self):
        print()

class Perro(Animal):
    def volar(self):
        raise TypeError("El perro no puede volar")

class Canario(Animal):
    ...
class Pato(Animal):
    ...
class PezVolador(Animal):
    def caminar(self):
        raise TypeError("Los peces no caminan")

        """

# Este diseño está mal implementado porque todos los animales
# dependen de la interfaz y hay que estar editando en base al animal.

# Para evitar esto, se utiliza el 4º principio SOLID:

# Interface Segregation Principle - Este principio nos dice que 
# una clase nunca debe extender de interfaces con métodos que no usa.

class Animal(ABC):
    def respirar(self):
        print("Estoy repirando")
    
    def comer(self):
        print("Estoy comiendo")

class AnimalesQueCaminan():
    def caminar(self):
        print("Estoy caminando")

class AnimalesQueVuelan():
    def volar(self):
        print("Estoy volando")

class AnimalesQueNadan():
    def nadar(self):
        print("Estoy nadando")


class Perro(Animal, AnimalesQueCaminan, AnimalesQueNadan):
    pass

class Canario(Animal, AnimalesQueCaminan, AnimalesQueVuelan):
    pass

class PezVolador(Animal, AnimalesQueNadan):
    pass