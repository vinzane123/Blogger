# Generated by Django 3.2 on 2023-12-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('publishedDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
