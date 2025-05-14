import re

# Clase donde se declara el producto y se validan los datos

class Producte:
    def __init__(self, codi: str, nom: str, preu: float, stock: int, categoria: str):
        if not re.match(r"^PROD-\d{4}$", codi):
            raise ValueError("Codi no vàlid. El format requerit es: PROD-XXXX")
        if categoria not in ["ELECTRONICA", "ROBA", "ALIMENTACIO"]:
            raise ValueError("Categoria no vàlida.")

        self.codi = codi
        self.nom = nom
        self.preu = preu
        self.stock = stock
        self.categoria = categoria