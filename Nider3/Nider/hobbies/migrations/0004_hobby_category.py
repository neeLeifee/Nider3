# Generated by Django 4.0 on 2022-04-05 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0003_hobbycategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hobbies.hobbycategory', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
