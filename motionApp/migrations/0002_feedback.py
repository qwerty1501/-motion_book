# Generated by Django 4.0.3 on 2022-03-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motionApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('url_project', models.URLField(blank=True, null=True, verbose_name='Укажите url путь youtube (*Не обязательно)')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
