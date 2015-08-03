# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('markdown', models.TextField()),
                ('html', models.TextField()),
                ('published', models.DateField()),
                ('updated', models.DateTimeField()),
            ],
        ),
    ]
