# Generated by Django 2.2.8 on 2020-10-30 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appawards', '0004_auto_20201030_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_upload',
            new_name='image',
        ),
    ]
