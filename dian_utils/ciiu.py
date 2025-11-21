import json
import unicodedata
from functools import lru_cache

try:
    # Python >=3.9
    from importlib.resources import files, as_file  # type: ignore
    _USE_FILES_API = True
except Exception:  # pragma: no cover
    # Python 3.7–3.8 fallback
    from importlib.resources import open_text  # type: ignore
    _USE_FILES_API = False


def _normalize(text: str) -> str:
    """
    Normaliza texto a minúsculas, sin acentos ni espacios extra.
    """
    text = text.strip().lower()
    nfkd = unicodedata.normalize("NFD", text)
    return "".join(c for c in nfkd if unicodedata.category(c) != "Mn")


@lru_cache()
def _load_ciiu_data() -> list:
    """
    Carga y cachea el contenido de `data/ciiu.json` incluido en el paquete.
    Funciona tanto en instalación editable como en wheel.
    """
    if _USE_FILES_API:
        with as_file(files("dian_utils.data").joinpath("ciiu.json")) as path:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    else:  # pragma: no cover
        with open_text("dian_utils.data", "ciiu.json", encoding="utf-8") as f:
            return json.load(f)


def list_ciiu() -> list:
    """
    Retorna la lista completa de códigos CIIU como objetos dict.
    Cada elemento puede tener las claves: `id`, `name` y opcionalmente `type`.
    """
    return _load_ciiu_data()


def get_ciiu_by_id(code: str) -> dict | None:
    """
    Busca un CIIU por su `id` exacto. Retorna el dict o `None` si no existe.
    """
    code_norm = code.strip()
    for item in _load_ciiu_data():
        if str(item.get("id", "")).strip() == code_norm:
            return item
    return None


def search_ciiu_by_prefix(prefix: str) -> list:
    """
    Retorna todos los CIIU cuyo `id` comienza con el `prefix` indicado.
    """
    pref = prefix.strip()
    return [it for it in _load_ciiu_data() if str(it.get("id", "")).startswith(pref)]


def search_ciiu_by_name(query: str, exact: bool = False) -> list:
    """
    Busca CIIU por nombre:
    - `exact=False` hace coincidencia por subcadena, insensible a acentos y mayúsculas.
    - `exact=True` compara por igualdad de nombre normalizado.
    Retorna una lista de dicts.
    """
    qn = _normalize(query)
    results = []
    for item in _load_ciiu_data():
        name = item.get("name", "")
        nn = _normalize(name)
        if exact:
            if nn == qn:
                results.append(item)
        else:
            if qn in nn:
                results.append(item)
    return results