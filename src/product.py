from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для класса Product"""

    @abstractmethod
    def __str__(self):
        pass


class Product(BaseProduct):
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

    def __str__(self):
        """Магический метод для строкового отображения"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения для получения полной стоимости всех товаров на складе"""
        if not isinstance(other, type(self)):
            raise TypeError("Нельзя складывать объекты разных классов!")
        return self.__price * self.quantity + other.__price * other.quantity

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
            product_data.get("name"),
            product_data.get("description"),
            product_data.get("price"),
            product_data.get("quantity"),
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


class Smartphone(Product):
    """Подкласс Smartphone от родительского класса Product"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        # Вызываем метод базового класса
        super().__init__(name, description, price, quantity)
        # Дополнительный код
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.model}, {self.color}. {self.price} руб. Остаток: {self.quantity} шт."


class LawnGrass(Product):
    """Подкласс LawnGrass от родительского класса Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        # Вызываем метод базового класса
        super().__init__(name, description, price, quantity)
        # Дополнительный код
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.country}, {self.color}. {self.price} руб. Остаток: {self.quantity} шт."
