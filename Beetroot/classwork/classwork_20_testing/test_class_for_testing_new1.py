from unittest import TestCase
from class_for_testing_new import Product, ProductStore


class TestProductStore(TestCase):
    def setUp(self) -> None:
        self.store = ProductStore()
        self.prod = Product('Sport', 'Football T-Shirt', 100)
        self.prod1 = Product('Food', 'Ramen', 1.5)
        self.prod2 = Product('Food', 'Bread', 4)
        self.prod3 = Product('Sport', 'Treadmill', 5000)

    def test_add__success(self):
        self.store.add(self.prod, 5)
        self.store.add(self.prod1, 10)
        self.assertEqual(self.store.products, {self.prod: 5, self.prod1:10}, 'Not equal products')

    def test_add__fail(self):
        with self.assertRaises(AttributeError):
            self.store.add('Sport', 10)

    def test_set_discount(self):
        self.store.add(self.prod1, 5)
        self.store.set_discount('Ramen', 30)
        self.assertEqual(self.prod1.price, 1.365, 'Not equal price')

    def test_sell_product(self):
        self.store.add(self.prod, 5)
        self.store.add(self.prod1, 10)
        self.store.sell_product('Football T-Shirt', 4)
        self.assertEqual(self.store.products, {self.prod: 1, self.prod1: 10}, 'Wrong')

    def test_get_income(self):
        self.store.add(self.prod, 5)
        self.store.sell_product('Football T-Shirt', 5)
        self.assertEqual(self.store.get_income(), 650.0, 'Wrong')


    def test_get_all_products(self):
        self.store.add(self.prod, 5)
        self.store.add(self.prod1, 10)
        self.assertEqual(self.store.get_all_products(), {self.prod: 5, self.prod1:10}, 'Wrong')

    def test_get_product_info(self):
        self.store.add(self.prod, 5)
        self.store.add(self.prod1, 10)
        self.store.sell_product('Football T-Shirt', 4)
        self.assertEqual(self.store.get_product_info('Football T-Shirt'), (self.prod, self.store.products[self.prod]))
