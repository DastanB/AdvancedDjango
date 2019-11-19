from django.db import models
import datetime
from main import constants
# Create your models here.
class ProductServiceBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class Product(ProductServiceBase):
    existence = models.BooleanField(default=True)
    product_type = models.PositiveSmallIntegerField(choices=constants.PRODUCT_TYPES, default=constants.PRODUCT_TSHIRT)
    size = models.PositiveSmallIntegerField(choices=constants.PRODUCT_SIZES, default=constants.PRODUCT_SMALL)

    class Meta:
        abstract = False

class Service(ProductServiceBase):
    aproximate_duration = models.DateField()
    service_type = models.PositiveSmallIntegerField(choices=constants.SERVICE_TYPES, default=constants.SERVICE_DELIVERY)

    class Meta:
        abstract = False