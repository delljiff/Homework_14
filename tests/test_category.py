import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def category_groceries():
    product1 = Product("Cucumber", "Green vegetable", 25.0, 10)
    product2 = Product("Tomato", "Red vegetable", 30.57, 12)
    product3 = Product("Onion", "Brown vegetable", 15.0, 20)
    product4 = Product("Potato", "Root vegetable", 20.0, 15)
    return Category("Groceries", "Vegetables", [product1, product2, product3, product4])


def test_init(category_groceries):
    assert category_groceries.name == "Groceries"
    assert category_groceries.description == "Vegetables"
    expected = "Cucumber, 25.0 руб. Остаток: 10 шт.\nTomato, 30.57 руб. Остаток: 12 шт.\nOnion, 15.0 руб. Остаток: 20 шт.\nPotato, 20.0 руб. Остаток: 15 шт."
    assert category_groceries.products == expected


def test_total_products_update(category_groceries):
    Category.total_products = 0  # Сбрасываем перед проверкой
    category_groceries.total_products_update()
    assert Category.total_products == 4


@pytest.fixture()
def reset_counters():
    """Сброс счетчиков категорий перед каждым тестом"""
    Category.total_categories = 0
    Category.total_products = 0
    yield
    Category.total_categories = 0
    Category.total_products = 0


def test_init_category(category_groceries):
    assert category_groceries.name == "Groceries"
    assert category_groceries.description == "Vegetables"

    assert category_groceries.products.count('\n') == 3  # 4 товара = 3 переноса

    assert len(category_groceries.products) > 0


def test_total_categories_increments(reset_counters):
    """Проверка, что при создании категории total_categories увеличивается"""
    assert Category.total_categories == 0

    Category("Cat1", "Desc1", [])
    assert Category.total_categories == 1

    Category("Cat2", "Desc2", [])
    assert Category.total_categories == 2

    Category("Cat3", "Desc3", [])
    assert Category.total_categories == 3


def test_total_products_updates_correctly(reset_counters):
    """Проверка, что total_products обновляется при создании категории"""
    assert Category.total_products == 0

    Category("Cat1", "Desc1", ["A", "B"])
    assert Category.total_products == 2

    Category("Cat2", "Desc2", ["C", "D", "E"])
    assert Category.total_products == 5  # Должно быть 2 + 3 = 5


def test_total_products_with_multiple_categories(reset_counters):
    """Проверка суммирования продуктов из нескольких категорий"""
    Category("Fruits", "Fresh", ["Apple", "Banana", "Orange"])
    assert Category.total_products == 3

    Category("Vegetables", "Green", ["Cucumber", "Tomato", "Onion", "Potato"])
    assert Category.total_products == 7  # 3 + 4 = 7

    Category("Dairy", "Milk products", ["Milk", "Cheese"])
    assert Category.total_products == 9  # 7 + 2 = 9


def test_total_products_with_empty_category(reset_counters):
    """Проверка, что пустая категория не меняет total_products"""
    Category("Fruits", "Fresh", ["Apple", "Banana"])
    assert Category.total_products == 2

    Category("Empty", "No products", [])
    assert Category.total_products == 2  # Должно остаться 2


def test_total_products_with_category_containing_product_objects(reset_counters):
    """Проверка подсчета с объектами Product"""
    from src.product import Product

    product1 = Product("Tomato", "Red", 30.57, 12)
    product2 = Product("Cucumber", "Green", 25.0, 8)
    product3 = Product("Onion", "Brown", 15.0, 20)

    Category("Groceries", "Vegetables", [product1, product2, product3])

    assert Category.total_products == 3


def test_total_categories_and_products_together(reset_counters):
    """Комплексная проверка обоих счетчиков"""
    assert Category.total_categories == 0
    assert Category.total_products == 0

    Category("Cat1", "Desc1", ["A", "B"])
    assert Category.total_categories == 1
    assert Category.total_products == 2

    Category("Cat2", "Desc2", ["C", "D", "E", "F"])
    assert Category.total_categories == 2
    assert Category.total_products == 6  # 2 + 4

    Category("Cat3", "Desc3", ["G"])
    assert Category.total_categories == 3
    assert Category.total_products == 7  # 6 + 1


def test_total_products_update_method(category_groceries):
    """Проверка работы метода total_products_update"""
    Category.total_categories = 0
    Category.total_products = 0

    category_groceries.total_products_update()
    assert Category.total_products == 4


@pytest.fixture()
def sample_products():
    """Фикстура с тестовыми продуктами"""
    return [
        Product("Cucumber", "Green vegetable", 25.0, 10),
        Product("Tomato", "Red vegetable", 30.57, 12),
        Product("Onion", "Brown vegetable", 15.0, 20),
    ]


@pytest.fixture()
def category_with_products(sample_products):
    """Фикстура с категорией и продуктами"""
    return Category("Groceries", "Vegetables", sample_products)


@pytest.fixture()
def empty_category():
    """Фикстура с пустой категорией"""
    return Category("Empty", "No products", [])


def test_products_getter_returns_string(category_with_products):
    """Проверяем, что геттер возвращает строку"""
    result = category_with_products.products
    assert isinstance(result, str)
    assert len(result) > 0


def test_products_getter_formats_correctly(category_with_products):
    """Проверяем правильность форматирования товаров"""
    result = category_with_products.products

    # Проверяем, что все товары есть в строке
    assert "Cucumber" in result
    assert "Tomato" in result
    assert "Onion" in result

    # Проверяем формат цены и остатка
    assert "25.0 руб." in result
    assert "30.57 руб." in result
    assert "Остаток: 10 шт." in result
    assert "Остаток: 20 шт." in result


def test_products_getter_empty_category(empty_category):
    """Проверяем, что для пустой категории возвращается сообщение"""
    result = empty_category.products
    assert result == "В категории нет товаров"


def test_products_getter_returns_multiline_string(category_with_products):
    """Проверяем, что для нескольких товаров возвращается многострочная строка"""
    result = category_with_products.products
    # Должно быть 2 переноса для 3 товаров (n-1 переносов)
    assert result.count('\n') == 2
