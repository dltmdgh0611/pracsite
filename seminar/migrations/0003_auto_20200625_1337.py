# Generated by Django 3.0.7 on 2020-06-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0002_roomforseminar_squashed_0007_auto_20200624_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='postofrecruitseminar',
            name='max_people_count',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postofrecruitseminar',
            name='min_people_count',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postofrecruitseminar',
            name='times_of_class',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plannedseminar',
            name='tag_string',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='roomforseminar',
            name='max_people_count',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='roomforseminar',
            name='min_people_count',
            field=models.SmallIntegerField(),
        ),
    ]