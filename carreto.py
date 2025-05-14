from producte import Producte
from collections import defaultdict

# Clase del carrito de compra para añadir los productos y con metodo estatico para aplicar el descuento

class Carreto:
    def __init__(self):
        self.productes = []

    def afegir_producte(self, producte: Producte):
        if producte.stock <= 0:
            raise ValueError("No hi ha stock disponible.")
        self.productes.append(producte)

    @staticmethod
    def aplicar_descomptes(productes):
        comptador = defaultdict(int)
        for p in productes:
            comptador[p.categoria] += 1

        total = 0
        for p in productes:
            preu = p.preu
            if comptador[p.categoria] >= 3:
                preu *= 0.85
            total += preu
        return round(total, 2)
