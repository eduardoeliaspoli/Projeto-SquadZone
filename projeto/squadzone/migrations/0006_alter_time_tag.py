# Generated by Django 5.1.1 on 2024-10-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadzone', '0005_rename_tipo_time_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='tag',
            field=models.CharField(choices=[('Casual', 'Casual'), ('Competitivo', 'Competitivo')], max_length=50),
        ),
    ]