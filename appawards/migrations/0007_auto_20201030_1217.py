# Generated by Django 2.2.8 on 2020-10-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appawards', '0006_auto_20201030_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='posted_project',
            new_name='project',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user_bio',
        ),
        migrations.AddField(
            model_name='image',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='', max_length=50),
        ),
    ]
