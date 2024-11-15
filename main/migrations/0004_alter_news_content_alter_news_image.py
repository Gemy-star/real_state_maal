# Generated by Django 5.1.1 on 2024-09-24 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_jobrequest_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
    ]
