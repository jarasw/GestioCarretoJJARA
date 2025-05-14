from producte import Producte
from carreto import Carreto
from gestor_comandes import GestorComandes

# Clase principal donde se crean los productos y se genera la factura

# Crear productes
p1 = Producte("PROD-1212", "Logitech G733 Lightspeed RGB Auriculares", 99.99, 5, "ELECTRONICA")
p2 = Producte("PROD-7645", "Razer Basilisk V3 Ratón", 54.99, 10, "ELECTRONICA")
p3 = Producte("PROD-0003", "Monitor AOC U34E2M 34 LED UltraWide", 295.00, 2, "ELECTRONICA")

# Crear el carretó i afegir els productes
carreto = Carreto()
carreto.afegir_producte(p1)
carreto.afegir_producte(p2)
carreto.afegir_producte(p3)

# Generar factura
gestor = GestorComandes()
gestor.generar_factura(carreto)

print("Factura generada correctament!")