# Generated by Django 2.2.8 on 2020-10-30 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appawards', '0003_auto_20201030_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_upload',
        ),
    ]