# Generated by Django 3.2.10 on 2022-05-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(upload_to='entries/'),
        ),
    ]
