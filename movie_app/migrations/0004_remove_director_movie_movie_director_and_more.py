# Generated by Django 4.2.4 on 2023-08-22 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_remove_movie_director_director_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movie_app.director'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.movie'),
        ),
    ]
