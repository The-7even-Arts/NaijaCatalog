# Generated by Django 4.2.5 on 2023-10-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_excelupload_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelupload',
            name='file',
            field=models.FileField(upload_to='catalogue/uploads/'),
        ),
    ]
