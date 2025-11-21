import sys
import os
import unittest

# Añadir la carpeta raíz al sys.path para pruebas locales
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dian_utils.ciiu import (
    list_ciiu,
    get_ciiu_by_id,
    search_ciiu_by_prefix,
    search_ciiu_by_name,
)


class TestCIIUFunctions(unittest.TestCase):

    def test_list_ciiu_has_items(self):
        data = list_ciiu()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('id', data[0])
        self.assertIn('name', data[0])

    def test_get_ciiu_by_id_exact(self):
        item = get_ciiu_by_id('0111')
        self.assertIsNotNone(item)
        self.assertEqual(item['id'], '0111')
        self.assertEqual(item['name'], 'Cultivo de cereales (excepto arroz), legumbres y semillas oleaginosas')

    def test_search_ciiu_by_prefix(self):
        items = search_ciiu_by_prefix('011')
        codes = {it['id'] for it in items}
        self.assertTrue({'0111', '0112', '0113'}.issubset(codes))

    def test_search_ciiu_by_name_accent_insensitive(self):
        # Debe encontrar "Cultivo de café" usando "cafe" sin tilde
        items = search_ciiu_by_name('cafe')
        ids = {it['id'] for it in items}
        self.assertIn('0123', ids)


if __name__ == '__main__':
    unittest.main()