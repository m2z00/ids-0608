# Generated by Django 2.1.15 on 2020-05-07 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='name',
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='city',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]