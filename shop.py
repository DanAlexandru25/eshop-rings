from pprint import pprint

products = []

class Product:


    def __init__(self, name, price, description='', stock=0):
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    def __str__(self) -> str:
        return f'{self.name} price ={self.price} stock={self.stock}'


    def __repr__(self):
        return str(self)


def print(menu):
    print(f'1. Adaugare produs')
    print(f'2. Lisetare produse')
    print(f'3. Cumparare produs')

def add_product():
    name = input('name=')
    price = float(input('price ='))
    description = input('description=')
    stock = int(input('stock='))
    product = Product(name, price, description, stock)
    products.append(product)


def list_product():
    pprint(products)


def list_products():
    pass


def interpret_command(comand):
    match command:
        case '1':
            add_product()
        case '2':
            list_products()
        

command = input('Introduceti o comada: ')


def print_menu():
    pass


while command != 'q':
    interpret_command(command)
    print_menu()
    command = input('Introduceti o comanda: ')
