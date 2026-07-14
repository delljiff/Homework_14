import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from category import Category
from product import LawnGrass, Product, Smartphone


@pytest.fixture()
def category_groceries():
    product1 = Product("Cucumber", "Green vegetable", 25.0, 10)
    product2 = Product("Tomato", "Red vegetable", 30.57, 12)
    product3 = Product("Onion", "Brown vegetable", 15.0, 20)
    product4 = Product("Potato", "Root vegetable", 20.0, 15)
    return Category("Groceries", "Vegetables", [product1, product2, product3, product4])


def test_total_products_update(category_groceries):
    Category.total_products = 0
    category_groceries.total_products_update()
    assert Category.total_products == 4


@pytest.fixture()
def reset_counters():
    Category.total_categories = 0
    Category.total_products = 0
    yield
    Category.total_categories = 0
    Category.total_products = 0


def test_init_category(category_groceries):
    assert category_groceries.name == "Groceries"
    assert category_groceries.description == "Vegetables"
    assert category_groceries.products.count("\n") == 3
    assert len(category_groceries.products) > 0


def test_total_categories_increments(reset_counters):
    assert Category.total_categories == 0
    Category("Cat1", "Desc1", [])
    assert Category.total_categories == 1
    Category("Cat2", "Desc2", [])
    assert Category.total_categories == 2
    Category("Cat3", "Desc3", [])
    assert Category.total_categories == 3


def test_total_products_updates_correctly(reset_counters):
    assert Category.total_products == 0
    Category("Cat1", "Desc1", ["A", "B"])
    assert Category.total_products == 2
    Category("Cat2", "Desc2", ["C", "D", "E"])
    assert Category.total_products == 5


def test_total_products_with_multiple_categories(reset_counters):
    Category("Fruits", "Fresh", ["Apple", "Banana", "Orange"])
    assert Category.total_products == 3
    Category("Vegetables", "Green", ["Cucumber", "Tomato", "Onion", "Potato"])
    assert Category.total_products == 7
    Category("Dairy", "Milk products", ["Milk", "Cheese"])
    assert Category.total_products == 9


def test_total_products_with_empty_category(reset_counters):
    Category("Fruits", "Fresh", ["Apple", "Banana"])
    assert Category.total_products == 2
    Category("Empty", "No products", [])
    assert Category.total_products == 2


def test_total_products_with_category_containing_product_objects(reset_counters):
    product1 = Product("Tomato", "Red", 30.57, 12)
    product2 = Product("Cucumber", "Green", 25.0, 8)
    product3 = Product("Onion", "Brown", 15.0, 20)
    Category("Groceries", "Vegetables", [product1, product2, product3])
    assert Category.total_products == 3


def test_total_categories_and_products_together(reset_counters):
    assert Category.total_categories == 0
    assert Category.total_products == 0
    Category("Cat1", "Desc1", ["A", "B"])
    assert Category.total_categories == 1
    assert Category.total_products == 2
    Category("Cat2", "Desc2", ["C", "D", "E", "F"])
    assert Category.total_categories == 2
    assert Category.total_products == 6
    Category("Cat3", "Desc3", ["G"])
    assert Category.total_categories == 3
    assert Category.total_products == 7


def test_total_products_update_method(category_groceries):
    Category.total_categories = 0
    Category.total_products = 0
    category_groceries.total_products_update()
    assert Category.total_products == 4


@pytest.fixture()
def sample_products():
    return [
        Product("Cucumber", "Green vegetable", 25.0, 10),
        Product("Tomato", "Red vegetable", 30.57, 12),
        Product("Onion", "Brown vegetable", 15.0, 20),
    ]


@pytest.fixture()
def category_with_products(sample_products):
    return Category("Groceries", "Vegetables", sample_products)


@pytest.fixture()
def empty_category():
    return Category("Empty", "No products", [])


def test_products_getter_returns_string(category_with_products):
    result = category_with_products.products
    assert isinstance(result, str)
    assert len(result) > 0


def test_products_getter_formats_correctly(category_with_products):
    result = category_with_products.products
    assert "Cucumber" in result
    assert "Tomato" in result
    assert "Onion" in result
    assert "25.0 руб." in result
    assert "30.57 руб." in result
    assert "Остаток: 10 шт." in result
    assert "Остаток: 20 шт." in result


def test_products_getter_empty_category(empty_category):
    result = empty_category.products
    assert result == "В категории нет товаров"


def test_products_getter_returns_multiline_string(category_with_products):
    result = category_with_products.products
    assert result.count("\n") == 2


def test_category_creation():
    p1 = Product("Ноутбук", "Игровой", 50000.0, 10)
    p2 = Product("Мышь", "Беспроводная", 1000.0, 25)
    category = Category("Электроника", "Всякая техника", [p1, p2])
    assert category.name == "Электроника"
    assert category.description == "Всякая техника"
    assert len(category._Category__products) == 2


def test_category_str():
    p1 = Product("Ноутбук", "Игровой", 50000.0, 10)
    p2 = Product("Мышь", "Беспроводная", 1000.0, 25)
    p3 = Product("Клавиатура", "Механическая", 3000.0, 7)
    category = Category("Электроника", "Всякая техника", [p1, p2, p3])
    expected = "Электроника, количество продуктов: 42 шт."
    assert str(category) == expected


def test_category_str_empty():
    category = Category("Пустая", "Нет товаров", [])
    expected = "Пустая, количество продуктов: 0 шт."
    assert str(category) == expected


def test_add_product():
    p1 = Product("Ноутбук", "Игровой", 50000.0, 10)
    p2 = Product("Мышь", "Беспроводная", 1000.0, 25)
    category = Category("Электроника", "Всякая техника", [p1])
    category.add_product(p2)
    assert len(category._Category__products) == 2
    total = sum(p.quantity for p in category._Category__products)
    assert total == 35


def test_add_product_duplicate():
    p1 = Product("Ноутбук", "Игровой", 50000.0, 10)
    category = Category("Электроника", "Всякая техника", [p1])
    category.add_product(p1)
    assert len(category._Category__products) == 1


def test_products_property():
    p1 = Product("Ноутбук", "Игровой", 50000.0, 10)
    p2 = Product("Мышь", "Беспроводная", 1000.0, 25)
    p3 = Product("Клавиатура", "Механическая", 3000.0, 7)
    category = Category("Электроника", "Всякая техника", [p1, p2, p3])
    expected = (
        "Ноутбук, 50000.0 руб. Остаток: 10 шт.\n"
        "Мышь, 1000.0 руб. Остаток: 25 шт.\n"
        "Клавиатура, 3000.0 руб. Остаток: 7 шт."
    )
    assert category.products == expected


def test_products_property_empty():
    category = Category("Пустая", "Нет товаров", [])
    assert category.products == "В категории нет товаров"


def test_total_categories_count():
    Category.total_categories = 0
    Category("Категория 1", "Описание", [])
    Category("Категория 2", "Описание", [])
    assert Category.total_categories >= 2


def test_add_product_to_empty_category():
    category = Category("Электроника", "Разная электроника", [])
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    category.add_product(product)
    assert "Ноутбук" in category.products
    assert "50000" in category.products
    assert "5" in category.products


def test_add_product_to_category_with_existing_products():
    existing_product = Product("Мышь", "Беспроводная мышь", 1500, 10)
    category = Category("Электроника", "Разная электроника", [existing_product])
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    category.add_product(product)
    assert "Ноутбук" in category.products
    assert "Мышь" in category.products


def test_add_smartphone_to_category():
    category = Category("Смартфоны", "Мобильные устройства", [])
    smartphone = Smartphone("iPhone", "Флагман", 80000, 3, "A15", "iPhone 13", "128GB", "Black")
    category.add_product(smartphone)
    assert "iPhone" in category.products


def test_add_lawn_grass_to_category():
    category = Category("Газоны", "Растения для газона", [])
    grass = LawnGrass("Газон", "Зеленый", 500, 100, "Россия", "7 дней", "Зеленый")
    category.add_product(grass)
    assert "Газон" in category.products


def test_add_duplicate_product_should_not_add():
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    category = Category("Электроника", "Разная электроника", [product])
    category.add_product(product)
    assert category.products.count("Ноутбук") == 1


def test_add_identical_products_different_instances():
    category = Category("Электроника", "Разная электроника", [])
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    product2 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    category.add_product(product1)
    category.add_product(product2)
    assert category.products.count("Ноутбук") == 2


def test_add_product_not_product_object_raises_type_error():
    category = Category("Электроника", "Разная электроника", [])
    with pytest.raises(TypeError, match="Можно добавлять продукты класса Product и дочерних от него"):
        category.add_product("Это строка")


def test_add_none_raises_type_error():
    category = Category("Электроника", "Разная электроника", [])
    with pytest.raises(TypeError, match="Можно добавлять продукты класса Product и дочерних от него"):
        category.add_product(None)


def test_add_integer_raises_type_error():
    category = Category("Электроника", "Разная электроника", [])
    with pytest.raises(TypeError, match="Можно добавлять продукты класса Product и дочерних от него"):
        category.add_product(123)


def test_add_list_raises_type_error():
    category = Category("Электроника", "Разная электроника", [])
    with pytest.raises(TypeError, match="Можно добавлять продукты класса Product и дочерних от него"):
        category.add_product(["Ноутбук", 50000])


def test_add_multiple_products_to_category():
    category = Category("Электроника", "Разная электроника", [])
    products = [
        Product("Ноутбук", "Мощный ноутбук", 50000, 5),
        Product("Мышь", "Беспроводная мышь", 1500, 10),
        Product("Клавиатура", "Механическая", 3000, 7),
    ]
    for product in products:
        category.add_product(product)
    for product in products:
        assert product.name in category.products


def test_add_product_does_not_affect_other_categories():
    category1 = Category("Электроника", "Разная электроника", [])
    category2 = Category("Книги", "Разные книги", [])
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    category1.add_product(product)
    assert "Ноутбук" in category1.products
    assert "Ноутбук" not in category2.products


def test_add_product_formats_output_correctly():
    category = Category("Электроника", "Разная электроника", [])
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    category.add_product(product)
    expected_format = "Ноутбук, 50000 руб. Остаток: 5 шт."
    assert expected_format in category.products


def test_add_products_of_different_types_to_same_category():
    category = Category("Товары", "Разные товары", [])
    product = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    smartphone = Smartphone("iPhone", "Флагман", 80000, 3, "A15", "iPhone 13", "128GB", "Black")
    grass = LawnGrass("Газон", "Зеленый", 500, 100, "Россия", "7 дней", "Зеленый")
    category.add_product(product)
    category.add_product(smartphone)
    category.add_product(grass)
    assert "Ноутбук" in category.products
    assert "iPhone" in category.products
    assert "Газон" in category.products
