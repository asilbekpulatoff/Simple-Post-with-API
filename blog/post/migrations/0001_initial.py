# Generated by Django 5.0.1 on 2024-01-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('content', models.TextField(max_length=500)),
                ('public', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='post_post_created_27aeb6_idx')],
            },
        ),
    ]
