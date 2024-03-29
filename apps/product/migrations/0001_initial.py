# Generated by Django 4.1 on 2023-02-10 15:24

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='photos')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
