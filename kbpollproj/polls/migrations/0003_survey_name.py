# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150527_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='name',
            field=models.CharField(max_length=64, default='First Survey'),
            preserve_default=False,
        ),
    ]
