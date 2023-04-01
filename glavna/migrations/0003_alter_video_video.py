# Generated by Django 4.1.7 on 2023-03-28 18:43

from django.db import migrations, models
import glavna.validators


class Migration(migrations.Migration):

    dependencies = [
        ('glavna', '0002_alter_video_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/video/', validators=[glavna.validators.validate_file_extension]),
        ),
    ]
