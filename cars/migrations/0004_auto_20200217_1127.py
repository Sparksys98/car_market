# Generated by Django 2.1.5 on 2020-02-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200217_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
