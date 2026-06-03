class Category:
    total_categories = 0
    total_products = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        self.total_products_update()

    def total_products_update(self):
        Category.total_products = len(self.products)