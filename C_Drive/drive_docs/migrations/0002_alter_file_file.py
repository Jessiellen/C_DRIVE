# Generated by Django 5.0.6 on 2024-06-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive_docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
