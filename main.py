from producte import Producte
from carreto import Carreto

# Clase principal donde se crean los productos y se genera la factura

# Crear productes
p1 = Producte("LOGI-1212", "Logitech G733 Lightspeed RGB Auriculares", 99.99, 5, "ELECTRONICA")
p2 = Producte("RAZE-7645", "Razer Basilisk V3 Ratón", 54.99, 10, "ELECTRONICA")
p3 = Producte("AOCI-0003", "Monitor AOC U34E2M 34 LED UltraWide", 295.00, 2, "ELECTRONICA")

# Crear el carretó i afegir els productes
carreto = Carreto()
carreto.afegir_producte(p1)
carreto.afegir_producte(p2)
carreto.afegir_producte(p3)
