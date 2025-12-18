import unittest
from app import app

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_product_list(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Ном", response.get_data(as_text=True))
        self.assertIn("Үзэг", response.get_data(as_text=True))

    def test_product_count(self):
        response = self.client.get("/products")
        self.assertIn("Нийт: 2", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
