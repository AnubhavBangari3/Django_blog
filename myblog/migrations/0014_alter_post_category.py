# Generated by Django 3.2.6 on 2021-09-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0013_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]
