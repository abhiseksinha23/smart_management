# Generated by Django 2.2.2 on 2019-08-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperate', '0014_auto_20190831_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankers',
            name='rank',
            field=models.PositiveIntegerField(),
        ),
    ]
