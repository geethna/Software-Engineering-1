# Generated by Django 2.2.10 on 2020-04-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_content_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='Notes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='content',
            name='Textbook',
            field=models.BooleanField(default=False),
        ),
    ]
