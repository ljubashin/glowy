# Generated by Django 4.1.7 on 2023-05-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glavna', '0006_alter_igdb_cover_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='igdb',
            name='cover_url',
            field=models.ImageField(null=True, upload_to='igdb/covers/'),
        ),
    ]
