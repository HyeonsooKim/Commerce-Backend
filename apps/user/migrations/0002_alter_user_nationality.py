# Generated by Django 4.1 on 2023-02-21 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nationality',
            field=models.ForeignKey(default=191, on_delete=django.db.models.deletion.CASCADE, related_name='user_nationality', to='user.nationality'),
        ),
    ]