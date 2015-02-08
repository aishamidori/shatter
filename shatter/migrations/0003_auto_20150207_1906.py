# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shatter', '0002_auto_20150207_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='tag_type',
        ),
        migrations.DeleteModel(
            name='Statistic',
        ),
    ]
