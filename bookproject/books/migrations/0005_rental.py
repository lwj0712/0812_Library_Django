# Generated by Django 5.1 on 2024-08-13 06:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField(auto_now_add=True, verbose_name='대여일')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='반납일')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='대여 도서')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='대여자')),
            ],
        ),
    ]
