from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название', help_text='Название сетевого узла')
    email = models.EmailField(verbose_name='Email', help_text='Адрес электронной почты')
    country = models.CharField(max_length=100, verbose_name='Страна', help_text='Страна сетевого узла')
    city = models.CharField(max_length=100, verbose_name='Город', help_text='Город сетевого узла')
    street = models.CharField(max_length=100, verbose_name='Улица', help_text='Улица сетевого узла')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома', help_text='Номер дома сетевого узла')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients',
                                 verbose_name='Поставщик', help_text='Поставщик сетевого узла')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Задолженность',
                               help_text='Задолженность по сетевому узлу')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень', help_text='Уровень сетевого узла')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',
                                      help_text='Дата создания сетевого узла')
    user = models.ForeignKey(get_user_model(), related_name='network_nodes', on_delete=models.CASCADE, null=True,
                             blank=True,
                             verbose_name='Пользователь')

    def get_admin_url(self):
        return reverse('admin:network_networknode_change', args=[self.pk])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сетевой узел'
        verbose_name_plural = 'Сетевые узлы'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', help_text='Название продукта')
    model = models.CharField(max_length=255, verbose_name='Модель', help_text='Модель продукта')
    release_date = models.DateField(verbose_name='Дата выпуска', help_text='Дата выпуска продукта')
    network_node = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, related_name='products',
                                     verbose_name='Сетевой узел', help_text='Сетевой узел для продукта')

    def get_admin_url(self):
        return reverse('admin:network_product_change', args=[self.pk])

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
