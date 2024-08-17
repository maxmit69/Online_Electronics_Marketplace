# Generated by Django 5.1 on 2024-08-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_remove_networknode_products_networknode_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networknode',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='network_nodes',
            field=models.ManyToManyField(help_text='Сетевые узлы', to='network.networknode', verbose_name='Сетевые узлы'),
        ),
    ]
