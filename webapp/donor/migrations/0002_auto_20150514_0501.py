# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offerrepetition',
            old_name='offer_id',
            new_name='offer',
        ),
    ]
