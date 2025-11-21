# dian-utils

Librería en Python para calcular el dígito de verificación del NIT/RUT según la DIAN en Colombia.

Incluye utilidades para consultar códigos CIIU empaquetados en `dian_utils/data/ciiu.json`.

Tomado del PDF de la resolución 000114 del 21-12-2020:
`
https://www.dian.gov.co/normatividad/Normatividad/Resoluci%C3%B3n%20000114%20de%2021-12-2020.pdf
`

## Instalación

```bash
pip install dian-utils
```

## Pruebas

```bash
python -m unittest discover tests
```

## Códigos CIIU

Ejemplos de uso:

```python
from dian_utils import (
    list_ciiu,
    get_ciiu_by_id,
    search_ciiu_by_prefix,
    search_ciiu_by_name,
)

# Listar todo
all_items = list_ciiu()

# Buscar por id exacto
item = get_ciiu_by_id('0111')

# Buscar por prefijo de id
items_pref = search_ciiu_by_prefix('011')

# Buscar por nombre (insensible a acentos y mayúsculas)
items_name = search_ciiu_by_name('cafe')  # encuentra "Cultivo de café"
```

## Licencia

Este proyecto se encuentra bajo la [Licencia MIT](https://opensource.org/license/mit).
