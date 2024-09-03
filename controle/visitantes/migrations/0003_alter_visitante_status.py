# Generated by Django 5.1 on 2024-09-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_visitante_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISITA', 'Em visita'), ('FINALIZADO', 'Visita finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
    ]
