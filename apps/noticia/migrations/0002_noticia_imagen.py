# Generated by Django 4.0.6 on 2022-07-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(default='noticia/default.png', upload_to='noticia'),
        ),
    ]
