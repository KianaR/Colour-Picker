# Generated by Django 4.2.3 on 2024-06-01 02:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('colour_picker_app', '0003_rename_image_image_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColourStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('colour_value', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
    ]