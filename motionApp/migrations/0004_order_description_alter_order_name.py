# Generated by Django 4.0.3 on 2022-04-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motionApp', '0003_createstaff_url_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
