# Generated by Django 4.0 on 2022-01-30 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='image',
            field=models.FileField(default='defaul.jpg', upload_to='games'),
        ),
    ]