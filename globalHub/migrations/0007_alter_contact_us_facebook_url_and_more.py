# Generated by Django 4.0.4 on 2022-06-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalHub', '0006_contact_us_facebook_url_contact_us_instagram_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='facebook_url',
            field=models.TextField(default='d'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='instagram_url',
            field=models.TextField(default='d'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='telegram_url',
            field=models.TextField(default='d'),
        ),
    ]
