# Generated by Django 3.0.4 on 2020-07-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0010_auto_20200704_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcrop',
            name='addContactNum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
