# Generated by Django 4.2.3 on 2024-05-31 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colour_picker_app', '0002_image_date_uploaded'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Image_Upload',
        ),
    ]