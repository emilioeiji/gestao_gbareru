# Generated by Django 4.0.3 on 2022-03-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(help_text='Nome do turno', max_length=100)),
            ],
        ),
    ]