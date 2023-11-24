# Generated by Django 4.1 on 2023-11-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название книги')),
                ('author', models.CharField(max_length=150, verbose_name='Имя автора')),
                ('publishing_year', models.PositiveSmallIntegerField(verbose_name='Год издания')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ('name',),
            },
        ),
    ]
