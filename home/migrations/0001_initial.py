# Generated by Django 3.2.6 on 2022-02-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('studio', models.CharField(max_length=25)),
                ('release_date', models.DateTimeField()),
            ],
        ),
    ]
