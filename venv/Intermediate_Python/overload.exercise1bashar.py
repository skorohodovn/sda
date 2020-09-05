class EshopCart:
    def __init__(self, buyer):
        self.buyer = buyer
        self.products = []
        self.total = 0.0

    def add_product(self, name, price):
        self.products.append(name)
        self.total += price

    def __add__(self, other):
        for product_name in other.products:
            self.add_product(product_name, 0)
        self.total += other.total
        return self

    def __len__(self):
        return len(self.products)

    def __str__(self):
        result = "EshopCart{ buyer:"
        result += self.buyer + ", products:"
        result += str(self.products) + ", total:"
        result += str(self.total) + "}"
        return result

    def __gt__(self, other):
        result = self.total > other.total
        return result

    def __lt__(self, other):
        result = self.total < other.total
        return result

    def __eq__(self, other):
        result = self.total == other.total
        return result

    def __contains__(self, item):
        result = item in self.products
        return result


if __name__ == "__main__":
    cart1 = EshopCart("Ann")
    cart1.add_product("jeans", 30.0)
    print(f"{cart1.buyer}'s Cart's length: {len(cart1)}")

    cart2 = EshopCart("Basar")
    cart2.add_product("laptop", 100.0)

    print(f"{cart2.buyer}'s Cart's length: {len(cart2)}")

    cart = cart1 + cart2
    string_cart = str(cart)
    print(string_cart)

    print(cart > cart2)
    print(cart < cart2)
    print(cart == cart2)

    print("jeans" in cart)