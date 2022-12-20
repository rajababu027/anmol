# Generated by Django 4.1.4 on 2022-12-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('office', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=10)),
                ('date', models.DateField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
