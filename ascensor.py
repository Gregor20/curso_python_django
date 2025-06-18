# CLASE ASCENSOR
# Esta clase simula un ascensor que puede subir y bajar entre pisos.
class ascensor:
    def __init__(self, max_piso): # Esto es el constructor de la clase, se ejecuta al crear una instancia (self es como "this" en java)
        self.max_piso = max_piso # Número máximo de pisos del ascensor
        if max_piso < 0:
            raise ValueError("El número máximo de pisos debe ser no negativo")
        self.piso_actual = 0 # Piso actual del ascensor, empieza en el 0
        self.pisos_pedidos=set()  # Conjunto de pisos pedidos, inicialmente vacío

    def pedir_piso(self, piso):
        if 0 <= piso <= self.max_piso:
            self.pisos_pedidos.add(piso)

    def ir_a_piso(self, destino):
        if not (0 <= destino <= self.max_piso):
            raise ValueError("Piso fuera de rango")
        
        if destino > self.piso_actual:
            self.subir(destino)
        elif destino < self.piso_actual:
            self.bajar(destino)
        else:
            print(f"Ya estás en el piso {destino}, no es necesario moverse.")

    def subir(self, destino):
        if not (0 <= destino <= self.max_piso):
            raise ValueError("Piso fuera de rango")

        for piso in range(self.piso_actual + 1, destino + 1):
            self.piso_actual = piso
            if piso in self.pisos_pedidos:
                print(f"Parando en el piso {piso}")
                self.pisos_pedidos.discard(piso)  # .discard() no lanza error si no está
            else:
                print(f"Subiendo al piso {piso} (sin parada)")

    def bajar(self, destino):
        if not (0 <= destino <= self.max_piso):
            raise ValueError("Piso fuera de rango")

        for piso in range(self.piso_actual - 1, destino - 1, -1):
            self.piso_actual = piso
            if piso in self.pisos_pedidos:
                print(f"Parando en el piso {piso}")
                self.pisos_pedidos.discard(piso)
            else:
                print(f"Bajando al piso {piso} (sin parada)")


if __name__ == "__main__":
    asc = ascensor(10)
    asc.pedir_piso(3)
    asc.pedir_piso(5)
    asc.ir_a_piso(7)
    asc.ir_a_piso(2)