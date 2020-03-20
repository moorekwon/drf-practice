# Generated by Django 2.2.11 on 2020-03-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='star_rating',
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='smoking',
            field=models.BooleanField(null=True),
        ),
    ]
