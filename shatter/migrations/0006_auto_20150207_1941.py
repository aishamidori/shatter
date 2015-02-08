# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shatter', '0005_auto_20150207_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(default=b'static/images/hab.svg', upload_to=b'test', blank=True),
            preserve_default=True,
        ),
    ]
