# Generated by Django 3.2.12 on 2023-12-18 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=128)),
                ('iin', models.BigIntegerField()),
                ('position', models.CharField(max_length=128)),
                ('contact', models.TextField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.financialorganization')),
            ],
        ),
    ]