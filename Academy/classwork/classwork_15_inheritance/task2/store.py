# Створити клас, який описує поняття "магазин"
# 1. Як називається клас? Shop
# 2. Які характеристики має? площа, назва, адрес, категорію магазину, словник товарів (к-сть значення)
# 3. Що поняття може робити? відкриватись/закриватись, поставка/продаж товарів, обслуговувати покупців

# Розширити функціонал класу Shop добавивши у нього розділ знижок
import datetime

class Product:
    def __init__(self, product_name: str, product_price: float):
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        return f"{self.product_name.capitalize()}: {self.product_price} UAH"
class Discount:
    def __init__(self, product, amount, due_to):
        self.product = product
        self.amount = amount
        self.due_to = due_to

    def count_discount(self, product):
        price = product.product_price
        if datetime.datetime.now() <= self.due_to:
            return price * (1 - self.amount / 100)
        else:
            return price

    def __str__(self):
        return self.product.product_name
class Shop:
    # площа, назва, адрес, категорію магазину, словник товарів (к-сть значення)
    def __init__(self, name, category, address, area):
        self.name = name
        self.category = category
        self.address = address
        self.area = area
        self.products = {} # продукт: [ціна, к-сть]
        self.status = False # відповідає за статус відкриття магазину
        self.discounts = []

    def open(self):
        self.status = True
        print(f'{self.name} is open')

    def close(self):
        self.status = False
        print(f'{self.name} is close')

    def change_status(self, status=True):
        self.status = status
        if status:
            print(f'{self.name} is open')
        else:
            print(f'{self.name} is close')

    def get_product(self, product, amount):
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount

    def sell_product(self, product, amount):
        if product in self.products and self.products[product] >= amount:
            self.products[product] -= amount
        else:
            print('Not enough product')
    @staticmethod
    def speak_up_with_customer(name):
        print(f'Speak up with {name}')

    def set_discount(self, product, amount, due_to):
        self.discounts.append(Discount(product, amount, due_to))

    def get_product_list(self):
        product_with_discount = [dis.product for dis in self.discounts]
        for product in self.products:
            if product in product_with_discount:
                index = product_with_discount.index(product)
                print(f'{product.product_name} price {self.discounts[index].count_discount(product)}')
            else:
                print(f'{product.product_name} price {product.product_price}')


if __name__ == '__main__':
    sun = Shop('Sun', 'grocery', 'Rivne', '50 square meters')
    moon = Shop('Moon', 'instrument', 'Rivne', '100 square meters')

    sun.open()
    moon.open()
    milk = Product('Milk', 10)
    sun.get_product(milk, 30)
    butter = Product('Butter', 30)
    sun.get_product(butter, 70)
    cheese = Product('Cheese', 100)
    sun.get_product(cheese, 100)
    tomato = Product('Tomato', 40)
    sun.get_product(tomato, 100)
    sun.speak_up_with_customer('Sofia')
    print(sun.products[milk])
    sun.get_product_list()
    sun.set_discount(cheese, 20, datetime.datetime(2023, 1, 15))
    sun.set_discount(milk, 5, datetime.datetime(2022, 12, 17))
    sun.set_discount(butter, 5, datetime.datetime(2022, 12, 15))
    sun.get_product_list()

