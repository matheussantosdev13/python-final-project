# Generated by Django 5.1 on 2024-09-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('PENDENTE', 'Pendente'), ('EM_VISITA', 'Em Visita'), ('FINALIZADO', 'Finalizado')], default='PENDENTE', max_length=20),
        ),
    ]
