# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyId', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('rating', models.CharField(max_length=2)),
                ('tag', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('employees', models.FloatField()),
                ('website', models.URLField()),
                ('diversity', models.DecimalField(max_digits=2, decimal_places=2)),
                ('comments', models.ManyToManyField(to='shatter.Comment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
