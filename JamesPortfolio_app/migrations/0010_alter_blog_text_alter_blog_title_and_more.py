# Generated by Django 4.1.1 on 2022-11-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JamesPortfolio_app', '0009_remove_blog_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]