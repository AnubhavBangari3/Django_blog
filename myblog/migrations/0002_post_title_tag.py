# Generated by Django 3.1 on 2020-09-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Blog', max_length=64),
        ),
    ]
