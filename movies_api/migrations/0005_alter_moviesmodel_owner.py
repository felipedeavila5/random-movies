# Generated by Django 4.0.3 on 2022-03-24 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies_api', '0004_alter_moviesmodel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesmodel',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]