# Generated by Django 2.0.5 on 2018-07-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180727_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='prerequisites',
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, null=True, to='main.Course'),
        ),
    ]
