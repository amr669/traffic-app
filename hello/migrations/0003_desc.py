# Generated by Django 4.1 on 2022-08-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_car_alter_greeting_id_alter_greeting_when_violation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('describe', models.CharField(max_length=50)),
            ],
        ),
    ]
