# Generated by Django 4.1.7 on 2023-03-17 17:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(null=True, upload_to='videos/thumbnails/')),
                ('video', models.FileField(blank=True, upload_to='videos/video/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glavna.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
