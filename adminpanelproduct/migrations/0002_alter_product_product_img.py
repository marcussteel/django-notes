# Generated by Django 4.1.1 on 2022-10-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanelproduct', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, default='images/logo.png', null=True, upload_to='product/'),
        ),
    ]