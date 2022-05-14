# Generated by Django 3.2 on 2022-05-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('horror', 'HORROR'), ('comedy', 'COMEDY'), ('action', 'ACCION'), ('drama', 'DRAMA')], max_length=10)),
            ],
        ),
    ]
