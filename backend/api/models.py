from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    """Represent a user profile inside our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Use to get a users full name """
        return f'{self.name}'

    def __str__(self):
        return f'{self.name} - {self.email}'

class Category(models.Model):
    name = models.CharField(_("category name"), max_length = 255)

    def __str__(self):
        return f"{self.name}"

        
class Product(models.Model):
    product_name = models.CharField(_("product name"), max_length = 255)
    product_image = models.ImageField(default='default.jpg', upload_to='product_imgs')
    product_desc = models.TextField(_("product description"))
    product_price = models.DecimalField(_("product price"), decimal_places = 2, max_digits=8)
    product_brand = models.CharField(_("product brand"), max_length = 255)
    product_category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}: {self.product_name}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.user}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cart}: {self.product}"