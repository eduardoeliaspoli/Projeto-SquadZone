# Generated by Django 5.1.1 on 2024-10-11 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squadzone', '0010_remove_usuario_groups_remove_usuario_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='verEmail',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='verSenha',
        ),
    ]
