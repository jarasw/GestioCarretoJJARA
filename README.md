Sistema de gestió de carretó de compra amb ofertes

Objectiu
Desenvolupar un sistema de carretó de compres per una coneguda botiga en línia que permeti:
Gestionar productes (afegir, eliminar, cercar).
Aplicar descomptes segons categoria.
Generar factures en format JSON.
Implementa validacions complexes i gestió d'errors.

Enunciat
Una reconeguda botiga en línia us ha contractat per crear un nou carretó de compra per a la seva web. El CEO de l'empresa ha fet arribar els requeriments generals, les funcionalitats obligatòries i els requeriments tècnics del sistema. Us ha donat 3 dies abans de quedar amb el CTO per a que validi la vostra solució.

Requeriments Generals:
Cada producte ha de tenir: códi (format PROD-XXXX, validat amb regex), nom, preu (double), stock (int), i categoria (ELECTRONICA, ROBA, ALIMENTACIO).
Objectes: Producte, Carreto, GestorComandes.
Fer servir TreeMap<String, Producte> per emmagatzemar productes a memòria (clave: códi).
Funcionalitats Obligatories:
Afegir un producte al carretó (validar stock > 0).
Aplicar descompte del 15% si hi ha 3+ productes de la mateixa categoria.
Guardar factures en un fitxer anomenat factures.json, l'estructura del fitxer la trobareu al fitxer adjunt a la tasca.
Requeriments Técnics:
Fer servir LocalDateTime per les factures.
Métode aplicarDescomptes() ha de ser static en carretó.
