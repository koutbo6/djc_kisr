# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_survey_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='choice',
            field=models.ForeignKey(default=0, to='polls.Choice'),
        ),
    ]
