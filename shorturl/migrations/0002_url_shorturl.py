# Generated by Django 3.0.3 on 2020-07-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='shorturl',
            field=models.URLField(default='https://bit.ly'),
            preserve_default=False,
        ),
    ]
