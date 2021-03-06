# Generated by Django 3.0.5 on 2020-04-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200416_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
