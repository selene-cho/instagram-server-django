# Generated by Django 4.1.7 on 2023-02-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_feed_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likesNum',
            field=models.PositiveIntegerField(default=0),
        ),
    ]