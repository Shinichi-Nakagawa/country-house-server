# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseMetrics',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('place', models.TextField()),
                ('temperature', models.FloatField()),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('memo', models.CharField(null=True, max_length=255)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='house_metrics')),
            ],
            options={
                'db_table': 'house_metrics',
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
