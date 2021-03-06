# Generated by Django 3.1.3 on 2021-01-18 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Бренд часов')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='media/watch/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материал',
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Пол',
                'verbose_name_plural': 'Пол',
            },
        ),
        migrations.CreateModel(
            name='ZipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип застёжки')),
            ],
            options={
                'verbose_name': 'Тип застёжки',
                'verbose_name_plural': 'Тип застёжки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название часов')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Цена')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('caliber', models.CharField(blank=True, max_length=30, null=True, verbose_name='Калибр/Механизм')),
                ('base_caliber', models.CharField(blank=True, max_length=30, null=True, verbose_name='Базовый калибр')),
                ('cruising_range', models.CharField(blank=True, max_length=30, null=True, verbose_name='Запас хода')),
                ('stones', models.CharField(blank=True, max_length=30, null=True, verbose_name='Количество камней')),
                ('back_cap', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прозрачная задняя крышка')),
                ('jewelry', models.BooleanField(blank=True, default=False, null=True, verbose_name='Отделка драгоценными камнями')),
                ('spraying', models.BooleanField(blank=True, default=False, null=True, verbose_name='PVD/DLS напыление')),
                ('dial1', models.BooleanField(blank=True, default=False, null=True, verbose_name='Гильошированный циферблат')),
                ('dial2', models.BooleanField(blank=True, default=False, null=True, verbose_name='Ручное гильоширование')),
                ('dial3', models.BooleanField(blank=True, default=False, null=True, verbose_name='Люминисцентные цифры')),
                ('chronograf', models.BooleanField(blank=True, default=False, null=True, verbose_name='Хронограф')),
                ('calendar_on_4_years', models.BooleanField(blank=True, default=False, null=True, verbose_name='Календарь на 4 года')),
                ('alarm_clock', models.BooleanField(blank=True, default=False, null=True, verbose_name='Будильник')),
                ('month_indicator', models.BooleanField(blank=True, default=False, null=True, verbose_name='Индикатор месяца')),
                ('year_calendar', models.BooleanField(blank=True, default=False, null=True, verbose_name='Годовой календарь')),
                ('eternal_calendar', models.BooleanField(blank=True, default=False, null=True, verbose_name='Вечный календарь')),
                ('gmt', models.BooleanField(blank=True, default=False, null=True, verbose_name='GMT/две часовые зоны')),
                ('jump_hour', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прыгающий час')),
                ('bracer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bracer', to='prod.material', verbose_name='Материал браслета')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.brand', verbose_name='Бренд')),
                ('corpus_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corpus_material', to='prod.material', verbose_name='Материал корпуса')),
                ('sex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.sex', verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Часы',
                'verbose_name_plural': 'Часы',
            },
        ),
    ]
