# Generated by Django 3.1.7 on 2021-03-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0004_auto_20210323_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='imdb_id',
            field=models.CharField(default='a', editable=False, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
