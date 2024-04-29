# Generated by Django 5.0.3 on 2024-04-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0004_remove_post_imageurl_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='post_images/'),
        ),
    ]