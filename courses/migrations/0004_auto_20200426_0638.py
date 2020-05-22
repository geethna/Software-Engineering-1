# Generated by Django 2.2.10 on 2020-04-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='rating',
        ),
        migrations.AddField(
            model_name='content',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]