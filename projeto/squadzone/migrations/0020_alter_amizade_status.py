# Generated by Django 5.1.1 on 2024-11-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadzone', '0019_remove_amizade_amizade_unica_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amizade',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Pendente', 'Pendente'), ('Recusado', 'Recusado')], max_length=50),
        ),
    ]
