# Generated by Django 4.1 on 2022-09-15 19:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('country_idx', models.IntegerField(primary_key=True, serialize=False)),
                ('country_code', models.CharField(max_length=10)),
                ('country_dcode', models.CharField(max_length=10)),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('email', models.EmailField(default='', max_length=100, unique=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('city', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('gender', models.CharField(blank=True, choices=[('Male', '남성'), ('Female', '여성')], max_length=6, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('nationality', models.ForeignKey(db_column='nationality', default=191, on_delete=django.db.models.deletion.CASCADE, related_name='user_nationality', to='user.nationality')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
