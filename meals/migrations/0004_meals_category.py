# Generated by Django 4.2 on 2023-04-24 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_category_alter_meals_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meals.category'),
        ),
    ]