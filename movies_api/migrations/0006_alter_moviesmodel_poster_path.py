# Generated by Django 4.0.3 on 2022-03-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0005_alter_moviesmodel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesmodel',
            name='poster_path',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
