# Generated by Django 2.2.4 on 2019-11-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tshirts', '0003_merge_20191108_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tshirt',
            old_name='tags',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='tshirt',
            old_name='topics',
            new_name='topic',
        ),
        migrations.RemoveField(
            model_name='tshirt',
            name='sex',
        ),
        migrations.AlterField(
            model_name='tshirt',
            name='image',
            field=models.ImageField(upload_to='uploads/images'),
        ),
    ]
