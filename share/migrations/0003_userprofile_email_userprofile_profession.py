# Generated by Django 5.1.6 on 2025-03-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_remove_userprofile_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]
