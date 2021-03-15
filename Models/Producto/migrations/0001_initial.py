# Generated by Django 3.1.7 on 2021-03-15 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Marca', '0001_initial'),
        ('Categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreproduc', models.CharField(max_length=75)),
                ('vencimiento', models.DateField()),
                ('nomcat', models.ForeignKey(max_length=75, on_delete=django.db.models.deletion.CASCADE, to='Categoria.categoria')),
                ('nommarc', models.ForeignKey(max_length=75, on_delete=django.db.models.deletion.CASCADE, to='Marca.marca')),
            ],
        ),
    ]
