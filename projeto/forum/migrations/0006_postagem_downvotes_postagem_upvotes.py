# Generated by Django 5.1.1 on 2024-11-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_remove_postagem_downvotes_remove_postagem_upvotes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postagem',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
