# Generated by Django 3.2.4 on 2022-06-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_remove_tache_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
