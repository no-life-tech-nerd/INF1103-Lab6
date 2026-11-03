from Product import Product
# import shared
from logging import warning

class Inventory:
    def __init__(self, products: list[Product]):
        self.products = products

    def int_input(self, numb: str) -> int:
        while True:
            try:
                return int(input(numb))
            except ValueError:
                warning("\nInput must be an integer, try again!\n")

    def display_all(self) -> None:
        print("Current Inventory")
        print("-----------------")

        for p in self.products:
            p.display_information()

        print("-----------------")

    def add_product(self, newProdId: int, newName: str, newPrice: float, newStock: int) -> Product | None:
        # TODO: port this back to main program
        # print("Add New Product")
        # print("---------------")
        # newProdId = self.int_input("Enter product ID: ")
        # newName = input("Enter product name: ")
        # try:
        #     newPrice = round(float(input("Enter product price: ")), 2)
        # except ValueError:
        #     warning("\nInput must be a float of up to 2 decimal places, try again!\n")
        #     return
        # newStock = self.int_input("Enter stock quantity: ")

        for p in self.products:
            if newProdId == p.get_product_id():
                warning("\nThis product ID already exists, try again!\n")
            elif newName == p.get_name():
                warning("\nThis product name already exists, try again!\n")

        try:
            self.products.append(Product(product_id = newProdId, name = newName, price = newPrice, stock = newStock))
            print("\nProduct added successfully!\n")
        except:
            print("\nUnknown error adding new product to inventory, try again!\n")
            return

    def update_product_stock(self, newProdId: int, newStock: int) -> None:
        # TODO: port this back to main program
        # print("Update Stock")
        # print("------------")
        # prodId = self.int_input("Enter product ID: ")
        for p in self.products:
            if newProdId == p.get_product_id():
                print("\nProduct found:\n")
                p.display_information()
                # p.update_stock(self.int_input("New Stock Quantity: ")) # TODO: port this too
                p.update_stock(newStock)
                if p.get_stock() > 500:
                    warning(f"There are more than 500 quantity of item {p.get_name()} in inventory!")
                return
        print("Product not found.")

