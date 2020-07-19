# Generated by Django 3.0.8 on 2020-07-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0003_auto_20200715_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postoffreeseminar',
            name='vote_count',
        ),
        migrations.RemoveField(
            model_name='postofrecruitseminar',
            name='vote_count',
        ),
        migrations.RemoveField(
            model_name='postofrequestseminar',
            name='vote_count',
        ),
        migrations.AddField(
            model_name='link',
            name='vote_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
