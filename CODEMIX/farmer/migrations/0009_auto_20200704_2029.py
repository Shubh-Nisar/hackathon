# Generated by Django 3.0.4 on 2020-07-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0008_auto_20200704_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcrop',
            name='id',
        ),
        migrations.AddField(
            model_name='addcrop',
            name='addPostNumber',
            field=models.Field(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]