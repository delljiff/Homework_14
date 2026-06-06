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
