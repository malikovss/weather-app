# Generated by Django 3.1.5 on 2021-01-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50)),
                ('day', models.TextField()),
                ('forecast', models.TextField()),
                ('forecast_desc', models.TextField()),
                ('humidity', models.TextField()),
                ('wind', models.TextField()),
                ('pressure', models.TextField()),
                ('moon', models.TextField()),
                ('sunrise', models.TextField()),
                ('sunset', models.TextField()),
                ('morning', models.TextField()),
                ('afternoon', models.TextField()),
                ('evening', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]