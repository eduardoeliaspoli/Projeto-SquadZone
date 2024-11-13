# Generated by Django 5.1.1 on 2024-11-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadzone', '0020_alter_amizade_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amizade',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Pendente', 'Pendente'), ('Recusado', 'Recusado')], default='Pendente', max_length=50),
        ),
    ]