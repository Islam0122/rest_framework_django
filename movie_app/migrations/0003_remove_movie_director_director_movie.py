# Generated by Django 4.2.4 on 2023-08-22 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_remove_movie_modified_data_remove_review_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='director',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movie_app.movie'),
            preserve_default=False,
        ),
    ]
