# Generated by Django 5.1.1 on 2024-10-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadzone', '0006_alter_time_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='verSenha',
            field=models.CharField(default='', max_length=255),
        ),
    ]