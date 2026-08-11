import pytest

from src.product import BaseProduct, LawnGrass, Product, ReprMixin, Smartphone


@pytest.fixture()
def product_tomato():
    return Product("Tomato", "Red", 30.57, 12)


def test_init(product_tomato):
    assert product_tomato.name == "Tomato"
    assert product_tomato.description == "Red"
    assert product_tomato.price == 30.57
    assert product_tomato.quantity == 12


def test_product_creation_with_different_values():
    """Тест создания продукта с другими значениями"""
    product = Product("Apple", "Sweet", 50.0, 5)

    assert product.name == "Apple"
    assert product.description == "Sweet"
    assert product.price == 50.0
    assert product.quantity == 5


def test_product_with_zero_quantity():
    """Тест продукта с нулевым количеством"""
    product = Product("Empty", "No stock", 10.99, 0)
    assert product.quantity == 0


def test_product_with_float_price():
    """Тест продукта с дробной ценой"""
    product = Product("Banana", "Yellow", 45.99, 10)
    assert product.price == 45.99
    assert isinstance(product.price, float)


def test_product_with_int_price():
    """Тест продукта с целой ценой"""
    product = Product("Orange", "Citrus", 100, 20)
    assert product.price == 100
    assert isinstance(product.price, int)


def test_product_attributes_types(product_tomato):
    """Тест типов атрибутов продукта"""
    assert isinstance(product_tomato.name, str)
    assert isinstance(product_tomato.description, str)
    assert isinstance(product_tomato.price, (int, float))
    assert isinstance(product_tomato.quantity, int)


@pytest.mark.parametrize(
    "name,description,price,quantity",
    [
        ("Bread", "Fresh baked", 50.0, 15),
        ("Milk", "3.2% fat", 80.5, 10),
        ("Cheese", "Hard cheese", 250.0, 5),
        ("Butter", "Salted", 120.0, 0),
    ],
)
def test_multiple_products(name, description, price, quantity):
    """Параметризованный тест для создания разных продуктов"""
    product = Product(name, description, price, quantity)

    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity


def test_new_product_creates_instance():
    """Проверяем, что new_product создает экземпляр Product"""
    product_data = {"name": "Laptop", "description": "Gaming laptop", "price": 1500.0, "quantity": 5}

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "Laptop"
    assert product.description == "Gaming laptop"
    assert product.price == 1500.0
    assert product.quantity == 5


def test_new_product_works_with_different_values():
    """Проверяем new_product с разными значениями"""
    product_data = {"name": "Phone", "description": "Smartphone", "price": 799.99, "quantity": 0}

    product = Product.new_product(product_data)

    assert product.name == "Phone"
    assert product.price == 799.99
    assert product.quantity == 0  # может быть 0


def test_product_creation():
    """Тест: создание продукта"""

    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    assert product.name == "Samsung Galaxy S23 Ultra", "Ошибка: имя не совпадает"
    assert product._Product__price == 180000.0, "Ошибка: цена не совпадает"  # обращаемся к приватному атрибуту
    assert product.quantity == 5, "Ошибка: количество не совпадает"


def test_product_str():
    """Тест: строковое отображение"""

    product = Product("Ноутбук", "Игровой", 50000.0, 10)

    expected = "Ноутбук, 50000.0 руб. Остаток: 10 шт."
    result = str(product)

    assert result == expected, f"Ошибка: ожидалось '{expected}', получили '{result}'"


def test_product_add():
    """Тест: сложение продуктов (общая стоимость)"""

    p1 = Product("Ноутбук", "Игровой", 50000.0, 10)
    p2 = Product("Мышь", "Беспроводная", 1000.0, 25)

    result = p1 + p2
    expected = (50000.0 * 10) + (1000.0 * 25)  # 525000

    assert result == expected, f"Ошибка: ожидалось {expected}, получили {result}"


def test_product_add_same():
    """Тест: сложение продукта с самим собой"""
    p = Product("Телефон", "Смартфон", 10000.0, 3)

    result = p + p
    expected = (10000.0 * 3) * 2  # 60000

    assert result == expected, f"Ошибка: ожидалось {expected}, получили {result}"


def test_add_two_products_same_class():
    """Тест сложения двух продуктов одного класса"""
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    product2 = Product("Мышь", "Беспроводная мышь", 1500, 10)

    result = product1 + product2
    expected = 50000 * 5 + 1500 * 10  # 250000 + 15000 = 265000

    assert result == expected


def test_add_two_smartphones():
    """Тест сложения двух смартфонов"""
    phone1 = Smartphone("iPhone", "Флагман", 80000, 3, "A15", "iPhone 13", "128GB", "Black")
    phone2 = Smartphone("Samsung", "Флагман", 70000, 4, "Exynos", "S22", "256GB", "White")

    result = phone1 + phone2
    expected = 80000 * 3 + 70000 * 4  # 240000 + 280000 = 520000

    assert result == expected


def test_add_two_lawn_grass_products():
    """Тест сложения двух продуктов LawnGrass"""
    grass1 = LawnGrass("Газон", "Зеленый", 500, 100, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газон премиум", "Изумрудный", 800, 50, "Германия", "5 дней", "Изумрудный")

    result = grass1 + grass2
    expected = 500 * 100 + 800 * 50  # 50000 + 40000 = 90000

    assert result == expected


def test_add_product_with_zero_quantity():
    """Тест сложения продуктов, где один имеет нулевое количество"""
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    product2 = Product("Мышь", "Беспроводная мышь", 1500, 0)

    result = product1 + product2
    expected = 50000 * 5 + 1500 * 0  # 250000

    assert result == expected


def test_add_product_with_one_quantity():
    """Тест сложения продуктов, где один имеет количество 1"""
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    product2 = Product("Мышь", "Беспроводная мышь", 1500, 1)

    result = product1 + product2
    expected = 50000 * 5 + 1500 * 1  # 251500

    assert result == expected


def test_add_same_product_instance():
    """Тест сложения продукта с самим собой"""
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    result = product + product
    expected = 50000 * 5 + 50000 * 5  # 500000

    assert result == expected


def test_add_product_and_string_raises_type_error():
    """Тест сложения продукта со строкой - должно вызывать TypeError"""
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    not_product = "Это строка"

    with pytest.raises(TypeError) as exc_info:
        product + not_product

    assert str(exc_info.value) == "Нельзя складывать объекты разных классов!"


def test_add_product_and_number_raises_type_error():
    """Тест сложения продукта с числом - должно вызывать TypeError"""
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)

    with pytest.raises(TypeError) as exc_info:
        product + 100

    assert str(exc_info.value) == "Нельзя складывать объекты разных классов!"


def test_add_product_and_none_raises_type_error():
    """Тест сложения продукта с None - должно вызывать TypeError"""
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)

    with pytest.raises(TypeError) as exc_info:
        product + None

    assert str(exc_info.value) == "Нельзя складывать объекты разных классов!"


def test_add_smartphone_and_lawn_grass_raises_type_error():
    """Тест сложения смартфона и газонной травы (разные дочерние классы) - должно вызывать TypeError"""
    smartphone = Smartphone("iPhone", "Флагман", 80000, 3, "A15", "iPhone 13", "128GB", "Black")
    grass = LawnGrass("Газон", "Зеленый", 500, 100, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError) as exc_info:
        smartphone + grass

    assert str(exc_info.value) == "Нельзя складывать объекты разных классов!"


def test_add_commutativity():
    """Тест коммутативности сложения (a + b == b + a)"""
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    product2 = Product("Мышь", "Беспроводная мышь", 1500, 10)

    result1 = product1 + product2
    result2 = product2 + product1

    assert result1 == result2


def test_add_with_large_numbers():
    """Тест сложения с большими числами"""
    product1 = Product("Сервер", "Мощный сервер", 1000000, 100)
    product2 = Product("СХД", "Система хранения", 2000000, 50)

    result = product1 + product2
    expected = 1000000 * 100 + 2000000 * 50  # 100000000 + 100000000 = 200000000

    assert result == expected


def test_add_with_float_prices():
    """Тест сложения продуктов с дробными ценами"""
    product1 = Product("Конфеты", "Сладкие", 150.50, 10)
    product2 = Product("Печенье", "Вкусное", 89.99, 5)

    result = product1 + product2
    expected = 150.50 * 10 + 89.99 * 5  # 1505 + 449.95 = 1954.95

    assert result == expected


def test_add_returns_number():
    """Тест, что результатом сложения является число (int или float)"""
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    product2 = Product("Мышь", "Беспроводная мышь", 1500, 10)

    result = product1 + product2

    assert isinstance(result, (int, float))


class TestBaseProduct:
    """Тесты для абстрактного базового класса"""

    def test_base_product_has_abstract_method(self):
        """Проверка наличия абстрактного метода __str__"""
        assert hasattr(BaseProduct, "__str__")
        # Проверяем, что метод абстрактный
        assert BaseProduct.__str__.__isabstractmethod__ is True

    def test_cannot_instantiate_base_product(self):
        """Проверка, что нельзя создать экземпляр абстрактного класса"""
        with pytest.raises(TypeError) as exc_info:
            BaseProduct()
        assert "Can't instantiate abstract class" in str(exc_info.value)


class TestReprMixin:
    """Тесты для миксина ReprMixin"""

    def test_repr_mixin_inheritance(self):
        """Проверка, что миксин можно использовать с другими классами"""

        class TestClass(ReprMixin):
            def __init__(self, name, description, price, quantity):
                self.name = name
                self.description = description
                self.price = price
                self.quantity = quantity
                super().__init__()

        obj = TestClass("Test", "Description", 100.5, 10)
        expected = "TestClass(Test, Description, 100.5, 10)"
        assert repr(obj) == expected

    def test_repr_mixin_with_different_types(self):
        """Проверка работы __repr__ с разными типами данных"""

        class TestClass(ReprMixin):
            def __init__(self, name, description, price, quantity):
                self.name = name
                self.description = description
                self.price = price
                self.quantity = quantity
                super().__init__()

        # Тест с целыми числами
        obj1 = TestClass("Item", "Desc", 50, 5)
        assert repr(obj1) == "TestClass(Item, Desc, 50, 5)"

        # Тест с числами с плавающей точкой
        obj2 = TestClass("Product", "Info", 99.99, 3)
        assert repr(obj2) == "TestClass(Product, Info, 99.99, 3)"

        # Тест со строками
        obj3 = TestClass("Name", "Long description with spaces", 0.0, 0)
        assert repr(obj3) == "TestClass(Name, Long description with spaces, 0.0, 0)"

    def test_repr_returns_string(self):
        """Проверка, что __repr__ возвращает строку"""

        class TestClass(ReprMixin):
            def __init__(self, name, description, price, quantity):
                self.name = name
                self.description = description
                self.price = price
                self.quantity = quantity
                super().__init__()

        obj = TestClass("Test", "Desc", 100, 10)
        assert isinstance(repr(obj), str)


def test_create_product_with_positive_quantity():
    """Тест: создание товара с положительным количеством"""
    product = Product("Телефон", "Смартфон", 50000, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.quantity == 10
    assert product._Product__price == 50000


def test_product_with_zero_quantity():
    """Тест продукта с нулевым количеством - должно выбрасываться исключение"""
    with pytest.raises(ValueError) as exc_info:
        Product("Empty", "No stock", 10.99, 0)

    # Проверяем, что сообщение об ошибке правильное
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


@pytest.mark.parametrize(
    "name,description,price,quantity,expect_error",
    [
        ("Bread", "Fresh baked", 50.0, 15, False),  # Должен создаться
        ("Milk", "3.2% fat", 80.5, 10, False),  # Должен создаться
        ("Cheese", "Hard cheese", 250.0, 5, False),  # Должен создаться
        ("Butter", "Salted", 120.0, 0, True),  # Должен выбросить ошибку
    ],
)
def test_multiple_products(name, description, price, quantity, expect_error):
    """Параметризованный тест для создания разных продуктов"""
    if expect_error:
        with pytest.raises(ValueError) as exc_info:
            Product(name, description, price, quantity)
        assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
    else:
        product = Product(name, description, price, quantity)
        assert product.name == name
        assert product.description == description
        assert product.quantity == quantity


def test_new_product_works_with_different_values():
    """Проверяем new_product с разными значениями"""
    # Тест с нулевым количеством - должна быть ошибка
    product_data_zero = {"name": "Phone", "description": "Smartphone", "price": 799.99, "quantity": 0}

    with pytest.raises(ValueError) as exc_info:
        Product.new_product(product_data_zero)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"

    # Тест с положительным количеством - должен создаться
    product_data_positive = {"name": "Phone", "description": "Smartphone", "price": 799.99, "quantity": 5}
    product = Product.new_product(product_data_positive)
    assert product.name == "Phone"
    assert product.quantity == 5


def test_add_product_with_zero_quantity():
    """Тест сложения продуктов, где один имеет нулевое количество"""
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)

    # Проверяем, что при создании продукта с нулевым количеством вылетает ошибка
    with pytest.raises(ValueError) as exc_info:
        Product("Мышь", "Беспроводная мышь", 1500, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"

    # Проверяем, что product1 создался нормально
    assert product1.quantity == 5
