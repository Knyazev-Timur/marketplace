# Generated by Django 4.2.3 on 2023-07-16 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('manufacturer', '0004_alter_manufacturer_owner_alter_manufacturer_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='owner',
            field=models.CharField(blank=True, choices=[('factory', 'Завод'), ('entrepreneur', 'Индивидуальный предприниматель'), ('seller', 'Торговая сеть')], default='factory', max_length=12, null=True),
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='product',
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
