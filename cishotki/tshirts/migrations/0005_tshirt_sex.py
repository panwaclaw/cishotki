# Generated by Django 2.2.4 on 2019-11-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tshirts', '0004_auto_20191108_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='sex',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
