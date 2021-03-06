# Generated by Django 4.0.4 on 2022-05-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.DateField()),
                ('tipo_de_pariente', models.CharField(choices=[('M', 'Madre'), ('P', 'Padre'), ('H', 'Hermano/a'), ('S', 'Sobrino/a')], default='H', max_length=1)),
                ('cantidad_de_hijos', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Familiar',
                'verbose_name_plural': 'Familiares',
            },
        ),
    ]
