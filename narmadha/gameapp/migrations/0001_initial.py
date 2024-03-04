# Generated by Django 5.0.2 on 2024-02-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_db',
            fields=[
                ('book_name', models.CharField(max_length=20)),
                ('author_name', models.CharField(max_length=20)),
                ('published_year', models.IntegerField(primary_key='published_year', serialize=False)),
                ('price', models.IntegerField()),
                ('ratings', models.IntegerField()),
            ],
        ),
    ]
