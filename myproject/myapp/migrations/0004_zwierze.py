# Generated by Django 5.1.2 on 2024-11-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_zamieszkanie_kod_pocztowy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zwierze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.IntegerField(choices=[(1, 'Pies'), (2, 'Kot'), (3, 'Kanarek'), (4, 'Chomik')])),
            ],
        ),
    ]
