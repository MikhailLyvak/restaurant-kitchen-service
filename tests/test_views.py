from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType, Dish


class PublicTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_dish_type_list_login_required(self):
        response = self.client.get(reverse("kitchen:dishtype-list"))

        self.assertNotEqual(response.status_code, 200)

    def test_dish_list_login_required(self):
        response = self.client.get(reverse("kitchen:dish-list"))

        self.assertNotEqual(response.status_code, 200)

    def test_cook_list_login_required(self):
        response = self.client.get(reverse("kitchen:cook-list"))

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="usertest", password="ban12345"
        )
        DishType.objects.create(name="Bread")
        DishType.objects.create(name="Soup")

        self.client.force_login(self.user)

    def test_dish_type_list(self):
        response = self.client.get(reverse("kitchen:dishtype-list"))
        dish_type_list = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishtype_list"]),
            list(dish_type_list),
        )
        self.assertTemplateUsed(response, "kitchen/dishtype_list.html")

    def test_dish_type_search(self):
        dish_type_filtered = DishType.objects.filter(
            name__icontains="Ces"
        )
        response = self.client.get(
            reverse("kitchen:dishtype-list"), {"name": "Ces"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishtype_list"]),
            list(dish_type_filtered),
        )

