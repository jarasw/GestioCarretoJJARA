import json
from datetime import datetime
from carreto import Carreto

class GestorComandes:
    def __init__(self):
        self.factures = []

    def generar_factura(self, carreto: Carreto):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        llista = [{"codi": p.codi, "preu": round(p.preu * 0.85, 2)
                  if self._te_descompte(p, carreto) else p.preu} for p in carreto.productes]
        total = Carreto.aplicar_descomptes(carreto.productes)
        factura = {"data": data, "productes": llista, "total": total}
        self.factures.append(factura)
        self._guardar_factura(factura)

    def _te_descompte(self, producte, carreto):
        return sum(1 for p in carreto.productes if p.categoria ==
                   producte.categoria) >= 3

    def _guardar_factura(self, factura):
        try:
            with open("factures.json", "r", encoding="utf-8") as f:
                dades = json.load(f)
        except FileNotFoundError:
            dades = []

        dades.append(factura)

        with open("factures.json", "w", encoding="utf-8") as f:
            json.dump(dades, f, indent=2, ensure_ascii=False)
