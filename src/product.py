class Product:
    """Класс для описания продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        """
        Класс-метод для создания нового продукта из словаря

        Args:
        product_data (dict): Словарь с данными товара
        Ожидаемые ключи: name, description, price, quantity

        Returns:
        Product: Новый экземпляр класса Product
        """
        return cls(
            product_data.get('name'),
            product_data.get('description'),
            product_data.get('price'),
            product_data.get('quantity')
        )

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для установки цены с проверкой"""
        if new_price <= 0:
            print(f"Цена не должна быть нулевая или отрицательная. Получено значение: {new_price}")
        else:
            self.__price = new_price
