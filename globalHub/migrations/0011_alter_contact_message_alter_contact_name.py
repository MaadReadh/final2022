# Generated by Django 4.0.4 on 2022-11-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalHub', '0010_contact_remove_order_code_remove_order_official_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]