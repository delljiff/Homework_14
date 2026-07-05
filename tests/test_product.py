import pytest

from src.product import Product


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
    product_data = {
        'name': 'Laptop',
        'description': 'Gaming laptop',
        'price': 1500.0,
        'quantity': 5
    }

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == 'Laptop'
    assert product.description == 'Gaming laptop'
    assert product.price == 1500.0
    assert product.quantity == 5


def test_new_product_works_with_different_values():
    """Проверяем new_product с разными значениями"""
    product_data = {
        'name': 'Phone',
        'description': 'Smartphone',
        'price': 799.99,
        'quantity': 0
    }

    product = Product.new_product(product_data)

    assert product.name == 'Phone'
    assert product.price == 799.99
    assert product.quantity == 0  # может быть 0


def test_product_creation():
    """Тест: создание продукта"""

    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    assert product.name == "Samsung Galaxy S23 Ultra", f"Ошибка: имя не совпадает"
    assert product._Product__price == 180000.0, f"Ошибка: цена не совпадает"  # обращаемся к приватному атрибуту
    assert product.quantity == 5, f"Ошибка: количество не совпадает"


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
