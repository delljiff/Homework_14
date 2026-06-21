# E-commerce приложение
* ***Модуль 1*** - Product. Класс для описания продуктов магазина.
* ***Модуль 2*** - Category. Класс для описания категорий.   
Пример:
```
{
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.get_category_count())
    print(category1.get_product_count())

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    for product in category2.products:
        print(product.name, product.description, product.price, product.quantity)

    print(Category.get_category_count())
    print(Category.get_product_count())

}

Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5
Iphone 15
512GB, Gray space
210000.0
8
Xiaomi Redmi Note 11
1024GB, Синий
31000.0
14
True
Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни
3
1
3
Телевизоры
Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником
1
[<product.Product object at 0x00000259731EE2C0>]
55" QLED 4K Фоновая подсветка 123000.0 7
2
4
```
## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/delljiff/Homework_14.git -b develop
```
2. Активация виртуального окружения:
```
poetry shell
```
3. Установка зависимостей:
```
poetry install 
```
4. Запуск проекта:
```
python main.py
```
## Тестирование:

1. Установка зависимостей
```
pip install pytest pytest-cov
```
2. Запуск всех тестов
```
pytest
```
3. Запуск каждого теста по отдельности
```
pytest tests/test_product.py
pytest tests/test_category.py
```
4. Запуск с отчетом о покрытии
```
poetry run pytest --cov 
```
## Удачи в использовании!