# Generated by Django 4.2.1 on 2023-06-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_comment_file1'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='img',
            field=models.ImageField(default='defaults/Books.jpeg', upload_to='image/'),
        ),
    ]