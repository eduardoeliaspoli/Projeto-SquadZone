# Generated by Django 5.1.1 on 2024-11-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_postagem_imagem_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='imagem_capa',
            field=models.ImageField(blank=True, upload_to='imagens_capa/'),
        ),
    ]