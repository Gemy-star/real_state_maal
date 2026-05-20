from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_chatbotqa'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecontent',
            name='home_first_paragrapgh_en',
            field=models.TextField(blank=True, null=True, verbose_name='First Paragraph (English)'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='roaya_paragraph_en',
            field=models.TextField(blank=True, null=True, verbose_name='Vision Paragraph (English)'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='messages_paragraph_en',
            field=models.TextField(blank=True, null=True, verbose_name='Messages Paragraph (English)'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='goals_paragraph_en',
            field=models.TextField(blank=True, null=True, verbose_name='Goals Paragraph (English)'),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='home_first_paragrapgh',
            field=models.TextField(blank=True, null=True, verbose_name='First Paragraph (Arabic)'),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='roaya_paragraph',
            field=models.TextField(blank=True, null=True, verbose_name='Vision Paragraph (Arabic)'),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='messages_paragraph',
            field=models.TextField(blank=True, null=True, verbose_name='Messages Paragraph (Arabic)'),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='goals_paragraph',
            field=models.TextField(blank=True, null=True, verbose_name='Goals Paragraph (Arabic)'),
        ),
    ]
