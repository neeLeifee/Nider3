# Generated by Django 4.0 on 2022-04-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='description',
            field=models.CharField(max_length=2048, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
    ]
