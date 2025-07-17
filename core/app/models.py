from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Car(models.Model):
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    engine_volume = models.CharField(max_length=100, default='Black')
    color = models.CharField(max_length=100, default='Black')
    transmission = models.CharField(max_length=100, default='Black')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    year_of_manufacture = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=100, default='Black')
    registration = models.CharField(max_length=100, default='Black')
    image = models.ImageField(upload_to='cars/images/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
