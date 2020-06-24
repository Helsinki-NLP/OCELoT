# pylint: disable=invalid-name,missing-docstring
# Generated by Django 2.2.13 on 2020-06-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('leaderboard', '0009_auto_20200618_2345')]

    operations = [
        migrations.AddField(
            model_name='testset',
            name='is_active',
            field=models.BooleanField(
                db_index=True,
                default=False,
                help_text='Is active test set?',
            ),
        )
    ]
