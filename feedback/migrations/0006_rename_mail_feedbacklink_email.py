# Generated by Django 4.0.3 on 2022-04-16 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_rename_question_feedbacklink_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbacklink',
            old_name='mail',
            new_name='email',
        ),
    ]