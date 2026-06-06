# E-commerce приложение
* ***Модуль 1*** - Product. Класс для описания продуктов магазина.
Пример:
```
{
if __name__ == '__main__':
    product_1 = Product('Tomato', 'Vegetables', 56.99, 67)
    print(product_1)
    print(product_1.name)
    print(product_1.description)
    print(product_1.price)
    print(product_1.quantity)
}

<__main__.Product object at 0x0000017CCC1086E0>
Tomato
Vegetables
56.99
67
```
* ***Модуль 2*** - Category. Класс для описания категорий. Пример:
```
{
if __name__ == '__main__':
    category_1 = Category('Groceries', 'Vegetables', ['Tomato', 'Cucumber', 'Onion', 'Carrot', 'Potato'])
    print(category_1)
    print(category_1.name)
    print(category_1.description)
    print(category_1.products)
    print(Category.total_products)
}

<__main__.Category object at 0x00000267FAC486E0>
Groceries
Vegetables
['Tomato', 'Cucumber', 'Onion', 'Carrot', 'Potato']
5

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