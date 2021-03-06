# Generated by Django 2.2.6 on 2019-11-10 14:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tshirts', '0006_auto_20191109_1635'),
        ('users', '0007_auto_20191109_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='tshirt',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tshirts.TShirt'),
            preserve_default=False,
        ),
    ]
