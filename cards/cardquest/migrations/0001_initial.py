# Generated by Django 5.0 on 2023-12-08 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonCard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('rarity', models.CharField(blank=True, choices=[('Common', 'Common'), ('Uncommon', 'Uncommon'), ('Rare', 'Rare')], max_length=100, null=True)),
                ('hp', models.IntegerField(blank=True, null=True)),
                ('card_type', models.CharField(blank=True, choices=[('Common', 'Common'), ('Uncommon', 'Uncommon'), ('Rare', 'Rare')], max_length=100, null=True)),
                ('attack', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('weakness', models.CharField(blank=True, max_length=250, null=True)),
                ('card_number', models.IntegerField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('evolution_stage', models.CharField(blank=True, max_length=250, null=True)),
                ('abilities', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('birthdate', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('collection_date', models.DateField()),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.pokemoncard')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.trainer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]