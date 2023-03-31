from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Dish, Cook, Ingredient, DishType


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    dish_type = forms.ModelChoiceField(queryset=DishType.objects.all(
    ), widget=forms.Select(attrs={'class': "info_header-text blur shadow-blur"}))

    class Meta:
        model = Dish
        fields = ["name", "price", "description",
                  "dish_type", "cooks", "ingredients"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "info_header-text blur shadow-blur",
                "placeholder": "name",
                "required": True
            }),
            "price": forms.TextInput(attrs={
                "class": "info_header-text blur shadow-blur",
                "placeholder": "price $"
            }),
            "description": forms.Textarea(attrs={
                "class": "info_desc blur shadow-blur",
                "placeholder": "Enter description here..."
            }),
        }


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name..."}
        )
    )


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_license_number(self):  # this logic is optional, but possible
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_license_number(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(years_of_experience,):
    if years_of_experience < 0:
        raise ValidationError("Experience years can`t be negative")
    elif not years_of_experience.is_integer():
        raise ValidationError("It should be integer value")

    return years_of_experience


class CookUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )
