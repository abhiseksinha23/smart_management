# Generated by Django 2.2.2 on 2019-08-31 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperate', '0011_faculties_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='pic',
            field=models.ImageField(upload_to='facultypic/'),
        ),
    ]
