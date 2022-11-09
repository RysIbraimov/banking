# Generated by Django 3.2 on 2022-11-08 14:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('accaunt_type', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('citizenship', models.CharField(default='Кыргызстан', max_length=20)),
                ('birth_year', models.DateField()),
                ('work_place', models.CharField(max_length=30)),
                ('update_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField()),
                ('date', models.DateField(verbose_name=datetime.date(2022, 11, 8))),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.client'),
        ),
    ]