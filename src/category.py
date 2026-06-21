class Category:
    """Класс для описания категорий"""

    total_categories = 0
    total_products = 0

    name: str
    description: str
    __products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        self.total_products_update()

    def total_products_update(self):
        Category.total_products += len(self.__products)

    def add_product(self, product):
        """Добавляет товар в категорию"""
        if product not in self.__products:
            self.__products.append(product)
            Category.total_products += 1

    @property
    def products(self):
        """Геттер для получения списка товаров в виде строки"""
        if not self.__products:
            return "В категории нет товаров"
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

        return "\n".join(result)

    @classmethod
    def get_category_count(cls):
        return cls.total_categories

    @classmethod
    def get_product_count(cls):
        return cls.total_products
