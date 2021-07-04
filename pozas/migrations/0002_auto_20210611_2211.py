# Generated by Django 3.2.2 on 2021-06-12 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pozas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poza',
            name='cantidad_gazapos',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='poza',
            name='cuyes_muertos',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='poza',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poza',
            name='peso_promedio',
            field=models.FloatField(default=0.0),
        ),
    ]