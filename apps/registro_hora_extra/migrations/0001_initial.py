# Generated by Django 3.1.3 on 2020-11-30 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroHoraExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100, verbose_name='Motivo')),
                ('hora_extra', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Hora Extra')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario')),
            ],
        ),
    ]
