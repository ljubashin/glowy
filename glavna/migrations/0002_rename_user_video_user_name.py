# Generated by Django 4.1.7 on 2023-04-25 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glavna', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='user',
            new_name='user_name',
        ),
    ]