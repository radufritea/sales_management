# Generated by Django 4.0.2 on 2022-05-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekplan',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='weekplan',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
