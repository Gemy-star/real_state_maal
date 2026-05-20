from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_homepagecontent_en_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Title (English)'),
        ),
        migrations.AddField(
            model_name='news',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Content (English)'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(verbose_name='Title (Arabic)'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(verbose_name='Content (Arabic)'),
        ),
    ]
