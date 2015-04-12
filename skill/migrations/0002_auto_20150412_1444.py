# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSkills',
            new_name='UserSkill',
        ),
    ]
