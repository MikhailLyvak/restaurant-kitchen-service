from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.conf import settings


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"
        ordering = ["-years_of_experience"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen:dish-detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False)
    amount = models.IntegerField(null=False)
    unit = models.CharField(max_length=255, null=False)
    
    class Meta:
        ordering = ["name"]
        constraints = [
            UniqueConstraint(
                fields=["name", "amount", "unit"],
                name="uniq_name_amount_unit"
            )
        ]

    def __str__(self):
        return f"{self.name} -> {self.amount} ({self.unit})"
        

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishs"
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="dishes"
    )

    class Meta:
        ordering = ["id"]
        

    def __str__(self):
        return self.name



        
