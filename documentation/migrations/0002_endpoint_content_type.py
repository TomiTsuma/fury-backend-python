# Generated by Django 2.2.6 on 2020-06-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='content_type',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
