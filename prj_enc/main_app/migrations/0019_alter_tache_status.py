# Generated by Django 3.2.4 on 2022-06-01 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_tache_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='status',
            field=models.IntegerField(),
        ),
    ]
