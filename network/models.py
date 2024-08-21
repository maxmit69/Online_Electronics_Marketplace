from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Address(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна', help_text='Страна предприятия')
    city = models.CharField(max_length=100, verbose_name='Город', help_text='Город предприятия')
    street = models.CharField(max_length=100, verbose_name='Улица', help_text='Улица предприятия')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома', help_text='Номер дома предприятия')

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название', help_text='Название предприятия')
    email = models.EmailField(verbose_name='Email', help_text='Email предприятия')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='network_nodes',
                                verbose_name='Адрес', help_text='Адрес предприятия')
    # country = models.CharField(max_length=100, verbose_name='Страна', help_text='Страна предприятия')
    # city = models.CharField(max_length=100, verbose_name='Город', help_text='Город предприятия')
    # street = models.CharField(max_length=100, verbose_name='Улица', help_text='Улица предприятия')
    # house_number = models.CharField(max_length=10, verbose_name='Номер дома', help_text='Номер дома предприятия')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients',
                                 verbose_name='Поставщик', help_text='Поставщик предприятия')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)],
                               verbose_name='Задолженность', help_text='Задолженность предприятия')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень', help_text='Уровень предприятия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',
                                      help_text='Дата создания предприятия')
    user = models.ForeignKey(get_user_model(), related_name='network_nodes', on_delete=models.CASCADE, null=True,
                             blank=True,
                             verbose_name='Пользователь')

    def get_admin_url(self):
        return reverse('admin:network_networknode_change', args=[self.pk])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'

    def calculate_level(self):
        """ Подсчет уровня предприятия на основе его поставщиков """
        level = 0
        supplier = self.supplier
        while supplier:
            level += 1
            supplier = supplier.supplier
        return level


# Сигнал для автоматического вычисления уровня перед сохранением объекта
@receiver(pre_save, sender=NetworkNode)
def set_hierarchy_level(sender, instance, **kwargs):
    instance.level = instance.calculate_level()


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', help_text='Название продукта')
    model = models.CharField(max_length=255, verbose_name='Модель', help_text='Модель продукта')
    release_date = models.DateField(verbose_name='Дата выпуска', help_text='Дата выпуска продукта')
    manufacturer = models.ManyToManyField(NetworkNode, related_name='products', verbose_name='Производитель',
                                          help_text='Предприятие, производитель продукта')

    def get_admin_url(self):
        return reverse('admin:network_product_change', args=[self.pk])

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
