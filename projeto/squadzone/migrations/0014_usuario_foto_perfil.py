# Generated by Django 5.1.1 on 2024-11-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadzone', '0013_remove_like_post_remove_like_user_remove_post_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, upload_to='imagens_perfil/'),
        ),
    ]