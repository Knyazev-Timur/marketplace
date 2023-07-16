# Generated by Django 4.2.3 on 2023-07-16 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('contacts', '0001_initial'),
        ('manufacturer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.contact'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='product',
            field=models.ManyToManyField(to='products.product'),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
