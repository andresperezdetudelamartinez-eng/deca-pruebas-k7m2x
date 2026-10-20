"""Generación de identificadores URL a partir de texto."""

import re
import unicodedata


def slugify(text: str) -> str:
    """Convierte un texto en un slug para URL.

    Pasa a minúsculas, translitera los acentos y la eñe, elimina los signos
    y separa las palabras con guiones.
    """
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text.strip("-")
