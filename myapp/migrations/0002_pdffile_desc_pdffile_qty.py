# Generated by Django 5.1.2 on 2024-10-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffile',
            name='desc',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pdffile',
            name='qty',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]