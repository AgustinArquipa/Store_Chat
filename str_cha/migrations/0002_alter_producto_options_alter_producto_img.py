# Generated by Django 4.2.3 on 2023-08-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('str_cha', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre', 'precio']},
        ),
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Foto'),
        ),
    ]
