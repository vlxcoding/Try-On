# shopping_cart/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import CartItem
from inventory.models import Product

class ShoppingCartTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=20.00)

    def test_cart_item_creation(self):
        cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)
        self.assertEqual(cart_item.subtotal_price, 40.00)
