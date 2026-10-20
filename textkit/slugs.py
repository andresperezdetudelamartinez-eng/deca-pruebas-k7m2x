"""Generación de identificadores URL a partir de texto."""

import re


def slugify(text: str) -> str:
    """Convierte un texto en un slug para URL.

    Pasa a minúsculas, elimina los signos y separa las palabras con guiones.
    """
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text.strip("-")
