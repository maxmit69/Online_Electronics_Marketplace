# Generated by Django 5.1 on 2024-08-21 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_networknode_city_alter_networknode_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='networknode',
            options={'verbose_name': 'Предприятие', 'verbose_name_plural': 'Предприятия'},
        ),
    ]
