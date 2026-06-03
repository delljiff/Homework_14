import pytest

from src.category import Category


@pytest.fixture()
def category_groceries():
    return Category('Groceries', 'Vegetables', ['Cucumber', 'Tomato', 'Onion', 'Potato'])


def test_init(category_groceries):
    assert category_groceries.name == 'Groceries'
    assert category_groceries.description == 'Vegetables'
    assert category_groceries.products == ['Cucumber', 'Tomato', 'Onion', 'Potato']


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
    assert category_groceries.name == 'Groceries'
    assert category_groceries.description == 'Vegetables'
    assert category_groceries.products == ['Cucumber', 'Tomato', 'Onion', 'Potato']


def test_total_categories_increments(reset_counters):
    """Проверка, что при создании категории total_categories увеличивается"""
    assert Category.total_categories == 0

    category1 = Category("Cat1", "Desc1", [])
    assert Category.total_categories == 1

    category2 = Category("Cat2", "Desc2", [])
    assert Category.total_categories == 2

    category3 = Category("Cat3", "Desc3", [])
    assert Category.total_categories == 3


def test_total_products_updates_correctly(reset_counters):
    """Проверка, что total_products обновляется при создании категории"""
    assert Category.total_products == 0

    category1 = Category("Cat1", "Desc1", ["A", "B"])
    assert Category.total_products == 2

    category2 = Category("Cat2", "Desc2", ["C", "D", "E"])
    assert Category.total_products == 5  # Должно быть 2 + 3 = 5


def test_total_products_with_multiple_categories(reset_counters):
    """Проверка суммирования продуктов из нескольких категорий"""
    cat1 = Category("Fruits", "Fresh", ["Apple", "Banana", "Orange"])
    assert Category.total_products == 3

    cat2 = Category("Vegetables", "Green", ["Cucumber", "Tomato", "Onion", "Potato"])
    assert Category.total_products == 7  # 3 + 4 = 7

    cat3 = Category("Dairy", "Milk products", ["Milk", "Cheese"])
    assert Category.total_products == 9  # 7 + 2 = 9


def test_total_products_with_empty_category(reset_counters):
    """Проверка, что пустая категория не меняет total_products"""
    cat1 = Category("Fruits", "Fresh", ["Apple", "Banana"])
    assert Category.total_products == 2

    cat2 = Category("Empty", "No products", [])
    assert Category.total_products == 2  # Должно остаться 2


def test_total_products_with_category_containing_product_objects(reset_counters):
    """Проверка подсчета с объектами Product"""
    from src.product import Product

    product1 = Product("Tomato", "Red", 30.57, 12)
    product2 = Product("Cucumber", "Green", 25.0, 8)
    product3 = Product("Onion", "Brown", 15.0, 20)

    category = Category("Groceries", "Vegetables", [product1, product2, product3])

    assert Category.total_products == 3


def test_total_categories_and_products_together(reset_counters):
    """Комплексная проверка обоих счетчиков"""
    assert Category.total_categories == 0
    assert Category.total_products == 0

    cat1 = Category("Cat1", "Desc1", ["A", "B"])
    assert Category.total_categories == 1
    assert Category.total_products == 2

    cat2 = Category("Cat2", "Desc2", ["C", "D", "E", "F"])
    assert Category.total_categories == 2
    assert Category.total_products == 6  # 2 + 4

    cat3 = Category("Cat3", "Desc3", ["G"])
    assert Category.total_categories == 3
    assert Category.total_products == 7  # 6 + 1


def test_total_products_update_method(category_groceries):
    """Проверка работы метода total_products_update"""
    Category.total_categories = 0
    Category.total_products = 0

    category_groceries.total_products_update()
    assert Category.total_products == 4