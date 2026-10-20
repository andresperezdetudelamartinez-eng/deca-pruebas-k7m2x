import unittest

from textkit.slugs import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hola Mundo"), "hola-mundo")

    def test_accents_are_transliterated(self):
        self.assertEqual(
            slugify("Murcia en 1820: ¡Qué calor!"),
            "murcia-en-1820-que-calor",
        )

    def test_enye(self):
        self.assertEqual(slugify("Peña de Alcantarilla"), "pena-de-alcantarilla")

    def test_symbols_removed(self):
        self.assertEqual(slugify("  --Hola, mundo!!  "), "hola-mundo")


if __name__ == "__main__":
    unittest.main()
