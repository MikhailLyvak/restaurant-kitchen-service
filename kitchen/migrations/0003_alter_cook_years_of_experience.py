# Generated by Django 4.1.7 on 2023-03-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0002_alter_cook_groups_alter_cook_user_permissions_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(null=True),
        ),
    ]
