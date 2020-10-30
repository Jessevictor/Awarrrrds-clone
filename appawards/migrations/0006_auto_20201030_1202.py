# Generated by Django 2.2.8 on 2020-10-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appawards', '0005_auto_20201030_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='project_description',
            new_name='posted_project',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='live_link',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_email',
        ),
        migrations.AddField(
            model_name='image',
            name='user_bio',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]