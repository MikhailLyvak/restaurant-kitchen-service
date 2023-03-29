from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.conf import settings


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return {self.name}


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(max_length=255)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"
        ordering = ["-years_of_experience"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cooks")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
