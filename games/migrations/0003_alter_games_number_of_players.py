# Generated by Django 4.1 on 2024-04-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_games_user_alter_games_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='number_of_players',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
