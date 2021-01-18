from django.db import models
from users.models import CustomUser
from django.utils.text import slugify


# модели для ForeignKey
class Sex(models.Model):
    name = models.CharField("Пол", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class Brand(models.Model):
    name = models.CharField("Бренд часов", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Material(models.Model):
    name = models.CharField("Материал", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материал'


class ZipType(models.Model):
    name = models.CharField("Тип застёжки", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип застёжки'
        verbose_name_plural = 'Тип застёжки'


class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField('Название часов', max_length=150)
    price = models.DecimalField('Цена', max_digits=15, decimal_places=2, null=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)
    year = models.IntegerField("Год выпуска", null=True, blank=True)
    sex = models.ForeignKey(
        Sex,
        on_delete=models.CASCADE,
        verbose_name='Пол',
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Бренд',
        null=True,
        blank=True,
    )

    # Калибр
    caliber = models.CharField('Калибр/Механизм', max_length=30, null=True, blank=True)
    base_caliber = models.CharField('Базовый калибр', max_length=30, null=True, blank=True)
    cruising_range = models.CharField('Запас хода', max_length=30, null=True, blank=True)
    stones = models.CharField('Количество камней', max_length=30, null=True, blank=True)

    # Корпус
    corpus_material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        verbose_name='Материал корпуса',
        related_name='corpus_material',
        null=True,
        blank=True,
    )
    back_cap = models.BooleanField('Прозрачная задняя крышка', null=True, blank=True, default=False)
    jewelry = models.BooleanField('Отделка драгоценными камнями', null=True, blank=True, default=False)

    # Циферблаит и стрелки
    spraying = models.BooleanField('PVD/DLS напыление', null=True, blank=True, default=False)
    dial1 = models.BooleanField('Гильошированный циферблат', null=True, blank=True, default=False)
    dial2 = models.BooleanField('Ручное гильоширование', null=True, blank=True, default=False)
    dial3 = models.BooleanField('Люминисцентные цифры', null=True, blank=True, default=False)

    # Браслет
    bracer = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        verbose_name='Материал браслета',
        related_name='bracer',
        null=True,
        blank=True,
    )
    zip_type = models.ForeignKey(
        ZipType,
        on_delete=models.CASCADE,
        verbose_name='Материал застёжки',
        null=True,
        blank=True,
    )
    zip_material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        verbose_name='Тип застёжки',
        related_name='zip_material',
        null=True,
        blank=True,
    )

    # Функции
    chronograf = models.BooleanField('Хронограф', null=True, blank=True, default=False)
    calendar_on_4_years = models.BooleanField('Календарь на 4 года', null=True, blank=True, default=False)
    alarm_clock = models.BooleanField('Будильник', null=True, blank=True, default=False)
    month_indicator = models.BooleanField('Индикатор месяца', null=True, blank=True, default=False)
    year_calendar = models.BooleanField('Годовой календарь', null=True, blank=True, default=False)
    eternal_calendar = models.BooleanField('Вечный календарь', null=True, blank=True, default=False)
    gmt = models.BooleanField('GMT/две часовые зоны', null=True, blank=True, default=False)
    jump_hour = models.BooleanField('Прыгающий час', null=True, blank=True, default=False)

    def get_image_filename(instance, filename):
        name = instance.post.name
        slug = slugify(name)
        return "post_images/%s-%s" % (slug, filename)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'


class Images(models.Model):
    ad = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/watch/%Y/%m/%d', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
