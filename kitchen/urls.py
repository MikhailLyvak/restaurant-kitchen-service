from django.urls import path

from .views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    toggle_assign_to_dish,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookExperienceUpdateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create", DishCreateView.as_view(), name="dish-create"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign"
    ),
    path("dishs/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishs/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/",
         CookExperienceUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("cooks/create", CookCreateView.as_view(), name="cook-create"),
    path(
        "dishtypes/",
        DishTypeListView.as_view(),
        name="dishtype-list",
    ),
    path(
        "dishtypes/create/",
        DishTypeCreateView.as_view(),
        name="dishtype-create",
    ),
    path(
        "dishtypes/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dishtype-update",
    ),
    path(
        "dishtypes/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dishtype-delete",
    ),
    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient-list",
    ),
    path(
        "ingredients/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
]



app_name = "kitchen"
