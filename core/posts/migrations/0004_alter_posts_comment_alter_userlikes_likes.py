# Generated by Django 4.2 on 2023-05-31 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posts_comments_alter_posts_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='comment',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='userlikes',
            name='likes',
            field=models.CharField(max_length=100000),
        ),
    ]
