class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.amount = None
        self.products = {}
        self.cash = 0

    def add(self, product, amount):
        self.amount = amount
        product.price *= 1.3
        self.products[product] = self.amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        for i in self.products:
            if identifier_type == 'name' and i.name == identifier:
                i.price *= (100 - percent) / 100
                break
            elif identifier_type == 'type' and i.type == identifier:
                i.price *= (100 - percent) / 100
                break

    def sell_product(self, product_name, amount):
        # sourcery skip: raise-specific-error
        for i in self.products:
            if i.name == product_name:
                if self.products[i] < amount:
                    raise Exception('We dont have so much of this product')
                self.products[i] -= amount
                self.cash += i.price * amount

    def get_income(self):
        print(self.cash)
        return self.cash

    def get_all_products(self):
        print(self.products)
        return self.products

    def get_product_info(self, product_name):
        for i in self.products:
            if i.name == product_name:
                print(i, self.products[i])
                return i, self.products[i]

