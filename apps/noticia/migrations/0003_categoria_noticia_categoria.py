# Generated by Django 4.0.6 on 2022-07-27 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_noticia_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='noticia.categoria'),
        ),
    ]