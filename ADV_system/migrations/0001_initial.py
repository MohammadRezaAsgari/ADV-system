# Generated by Django 4.0.6 on 2022-07-25 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('site', models.URLField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('img', models.URLField(max_length=250)),
                ('link', models.URLField(max_length=250)),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADV_system.advertiser')),
            ],
        ),
    ]
