# Generated by Django 4.1.1 on 2022-11-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JamesPortfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]
