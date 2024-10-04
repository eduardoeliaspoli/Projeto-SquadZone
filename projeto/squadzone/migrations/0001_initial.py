# Generated by Django 5.1.1 on 2024-09-30 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('brincadeira', 'Brincadeira'), ('tryhard', 'Tryhard')], max_length=50)),
                ('escudo', models.ImageField(upload_to='escudos/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('localizacao', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('nivel_reputacao', models.IntegerField(default=0)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_treino', models.DateField()),
                ('hora', models.TimeField()),
                ('time_1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treinos_time_1', to='squadzone.time')),
                ('time_2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treinos_time_2', to='squadzone.time')),
            ],
        ),
        migrations.AddField(
            model_name='time',
            name='criador_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='squadzone.usuario'),
        ),
        migrations.CreateModel(
            name='PerfilJogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('modalidade', models.CharField(choices=[('casual', 'Casual'), ('competitivo', 'Competitivo')], max_length=50)),
                ('jogo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='squadzone.jogo')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='squadzone.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Mentoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=255)),
                ('data_mentoria', models.DateField()),
                ('usuario_experiente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_experiente', to='squadzone.usuario')),
                ('usuario_novato_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_novato', to='squadzone.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='JogadorTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.CharField(max_length=255)),
                ('data_entrada', models.DateField()),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('time_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='squadzone.time')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='squadzone.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('data_postagem', models.DateTimeField(auto_now_add=True)),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='squadzone.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('data_recebido', models.DateTimeField(blank=True, null=True)),
                ('usuario_enviou_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_enviados', to='squadzone.usuario')),
                ('usuario_recebeu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_recebidos', to='squadzone.usuario')),
            ],
        ),
    ]
