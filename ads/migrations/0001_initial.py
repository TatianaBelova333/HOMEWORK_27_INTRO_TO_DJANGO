# Generated by Django 4.1 on 2022-08-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('author', models.CharField(default='', max_length=30)),
                ('price', models.CharField(default=0, max_length=30)),
                ('description', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=200)),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
