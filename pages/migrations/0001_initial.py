# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-14 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('micro_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(blank=True, max_length=100, null=True)),
                ('domain_url', models.URLField(blank=True, null=True)),
                ('country', models.CharField(max_length=100)),
                ('enquery_type', models.CharField(choices=[(b'general', b'Request For Services'), (b'partnership', b'Partnership Queries'), (b'media', b'Media Queries'), (b'general queries', b'General Queries'), (b'feedback', b'Website Feedback'), (b'others', b'Others')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, default=b'off', max_length=5)),
                ('lvl', models.IntegerField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.SlugField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_description', models.TextField()),
                ('keywords', models.TextField()),
                ('category', models.ManyToManyField(to='micro_blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='simplecontact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('contacted_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.simplecontact'),
        ),
    ]
