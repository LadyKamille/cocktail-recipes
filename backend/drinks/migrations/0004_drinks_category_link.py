# Generated by Django 3.1.4 on 2020-12-27 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='category_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drinks.category'),
        ),
    ]