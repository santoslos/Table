# Generated by Django 3.1.6 on 2021-05-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('distance', models.IntegerField(verbose_name='Расстояние')),
            ],
        ),
    ]
