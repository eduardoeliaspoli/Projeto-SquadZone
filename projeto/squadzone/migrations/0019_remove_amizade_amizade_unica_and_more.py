# Generated by Django 5.1.1 on 2024-11-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadzone', '0018_amizade_data_criacao'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='amizade',
            name='amizade_unica',
        ),
        migrations.RenameField(
            model_name='amizade',
            old_name='usuario_2',
            new_name='amigo',
        ),
        migrations.RenameField(
            model_name='amizade',
            old_name='usuario_1',
            new_name='usuario',
        ),
        migrations.AddConstraint(
            model_name='amizade',
            constraint=models.UniqueConstraint(fields=('usuario', 'amigo'), name='amizade_unica'),
        ),
    ]