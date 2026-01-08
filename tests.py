import unittest  
from models import Product

class TestModels(unittest.TestCase):
    def test_product_total_cost(self):
        product = Product("Test", "Category", 10, 5.0)
        self.assertEqual(product.total_cost(), 50.0)

    # def test_operation_creation(self):
    #     product = Product("Test", "Category", 10, 5.0)
    #     operation = Product("incoming", product)
    #     self.assertEqual(product.name, "Test")

if __name__ == "__main__":
    unittest.main()