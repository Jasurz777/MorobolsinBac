# Generated by Django 4.1.7 on 2023-03-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0004_color_alter_product_price_type_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[('sum', 'sum'), ('₽', '₽'), ('$', '$')], max_length=5),
        ),
    ]
