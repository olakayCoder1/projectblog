# Generated by Django 4.0 on 2022-01-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_posts_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
