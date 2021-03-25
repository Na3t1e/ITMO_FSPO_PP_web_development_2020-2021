# Generated by Django 3.1.7 on 2021-03-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ownering',
            new_name='Owning',
        ),
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.ManyToManyField(through='blog.Owning', to='blog.Owner'),
        ),
    ]