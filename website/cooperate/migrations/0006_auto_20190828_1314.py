# Generated by Django 2.2.2 on 2019-08-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperate', '0005_centers_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculties',
            name='qualification',
            field=models.CharField(default='B.tech', max_length=300),
        ),
        migrations.AddField(
            model_name='faculties',
            name='salary',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='feestatus',
            field=models.CharField(default='Not paid', max_length=50),
        ),
    ]