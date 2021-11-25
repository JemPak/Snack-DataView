# Generated by Django 3.2.9 on 2021-11-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField(default=0)),
                ('price', models.BigIntegerField()),
                ('description', models.TextField(max_length=2000)),
                ('url_image', models.URLField(max_length=2000)),
            ],
        ),
    ]