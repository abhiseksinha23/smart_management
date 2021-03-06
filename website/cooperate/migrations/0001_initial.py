# Generated by Django 2.2.2 on 2019-08-28 07:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('created_data', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
    ]
