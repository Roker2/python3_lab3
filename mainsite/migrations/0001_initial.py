# Generated by Django 3.0.5 on 2020-04-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('url', models.TextField()),
            ],
        ),
    ]
