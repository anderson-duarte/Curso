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
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('arquivo', models.FileField(upload_to='documentos')),
                ('pertence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario')),
            ],
        ),
    ]
