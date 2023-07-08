class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

        def get_details(self):
            raise NotImplementedError("Subclass must implement get_details method")
class Book(Product):
    def __init__(self, name, price,author):
        super().__init__(name,price)
        self.author = author
        
    def get_details(self):
        return f"Book: {self.name}, Author: {self.author}, Price: {self.price}"

class Electronic(Product):
    def __init__(self, name, price, brand):
        super().__init__(name,price)
        self.brand = brand
    def get_details(self):
        return f"Electronic: {self.name}, Brand: {self.brand}, Price: {self.price}"
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name,price)
        self.size = size
    
    def get_details(self):
        return f"Clothing: {self.name}, Size: {self.size}, Price: {self.price}"
    
products = [
    Book("Harry Potter", 29.99, "J.K. Rowling"),
    Electronic("Smart Phone", 500.00, "Tecno"),
    Clothing("T-shirt", 120.00, "XXL"),
]

for product in products:
    print(product.get_details())