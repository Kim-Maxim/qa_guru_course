"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000)
        assert product.check_quantity(999)
        assert product.check_quantity(1001) == False
        assert product.check_quantity(500)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(300)

        assert product.check_quantity(700)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_card_add_product(self, product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1

        cart.add_product(product, 6)
        assert cart.products[product] == 7

    def test_card_remove_product(self, product, cart):
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        assert cart.products[product] == 1

        cart.remove_product(product)
        cart.add_product(product, 3)
        cart.remove_product(product, 4)
        assert product not in cart.products

        cart.add_product(product, 2)
        cart.remove_product(product)
        assert product not in cart.products

    def test_card_clear(self, product, cart):
        cart.add_product(product, 10)
        cart.clear()

        assert product not in cart.products

    def test_cart_get_total_price(self, product, cart):
        cart.add_product(product, 7)
        assert cart.get_total_price() == 700

        cart.remove_product(product, 5)
        assert cart.get_total_price() == 200

        cart.remove_product(product)
        assert cart.get_total_price() == 0

    def test_cart_buy(self, product, cart):
        cart.add_product(product, 12)
        cart.buy()
        assert product.quantity == 988

        product.quantity = 1000
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()

        product.quantity = 0
        cart.add_product(product, 2)
        with pytest.raises(ValueError):
            cart.buy()
        