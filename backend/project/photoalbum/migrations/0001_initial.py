# Generated by Django 3.2.10 on 2022-02-22 11:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('pub_date', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(upload_to='entries/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='photoalbum.album')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]
