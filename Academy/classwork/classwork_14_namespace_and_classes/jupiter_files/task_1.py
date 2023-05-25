class Shop:
    def __init__(self, name:str, area:int or float, address:str, category:str):
        self.name = name
        self.area = area
        self.address = address
        self.category = category
        self.status = 'close'
        self.goods = {}

    def open(self):
        self.status = 'open'
        print(f'{self.name.capitalize()}  is {self.status} now.')

    def close(self):
        self.status = 'close'
        print(f'{self.name.capitalize()}  is {self.status} now.')


    def set_goods(self, goods_dict: dict):
        self.goods = goods_dict

    def get_product(self, name_product, amount_product):
        if name_product in self.goods:
            self.goods[name_product] += amount_product
        else:
            self.goods[name_product] = amount_product

    def sell_products(self, name_product, amount_product):
        if name_product in self.goods and self.goods.get(name_product, 0 >= amount_product):
            self.goods[name_product] -= amount_product
        else:
            print('Not enough products')

    def show_stock(self):
        for i, v in self.goods.items():
            print(f"{v} of {i} in stock")

    @staticmethod
    def speak_up_with_customer(customer_name):
        print(f'Hello, {customer_name}!')


if __name__ == '__main__':
    fun = Shop('Fun Shoes',100,'Kyiv','shoes shop')
    fun.open()
    fun.set_goods({
       'boots': 10,
       'sneakers': 5,})
    fun.show_stock()
    fun.speak_up_with_customer('Serhii')






