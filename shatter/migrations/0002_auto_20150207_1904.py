# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shatter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='statistic',
            name='tag_type',
            field=models.ForeignKey(to='shatter.Tag_Type', null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='comment',
            name='companyId',
        ),
        migrations.RemoveField(
            model_name='company',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='company',
            name='employees',
        ),
        migrations.AddField(
            model_name='comment',
            name='company',
            field=models.ForeignKey(to='shatter.Company', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='inclusivity',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='overall_rating',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='percent_women',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='tag',
            field=models.ForeignKey(to='shatter.Tag_Type', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='diversity',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
