# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('draw', '0001_initial'),
        ('adjfeedback', '0002_auto_20171110_0905'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='adjudicatorfeedback',
            name='source_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='draw.DebateTeam', verbose_name='source team'),
        ),
        migrations.AddField(
            model_name='adjudicatorfeedback',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adjfeedback_adjudicatorfeedback_submitted', to=settings.AUTH_USER_MODEL, verbose_name='submitter'),
        ),
        migrations.AlterUniqueTogether(
            name='adjudicatorfeedbackstringanswer',
            unique_together=set([('question', 'feedback')]),
        ),
        migrations.AlterUniqueTogether(
            name='adjudicatorfeedbackquestion',
            unique_together=set([('tournament', 'seq'), ('tournament', 'reference')]),
        ),
        migrations.AlterUniqueTogether(
            name='adjudicatorfeedbackintegeranswer',
            unique_together=set([('question', 'feedback')]),
        ),
        migrations.AlterUniqueTogether(
            name='adjudicatorfeedbackfloatanswer',
            unique_together=set([('question', 'feedback')]),
        ),
        migrations.AlterUniqueTogether(
            name='adjudicatorfeedbackbooleananswer',
            unique_together=set([('question', 'feedback')]),
        ),
        migrations.AlterUniqueTogether(
            name='adjudicatorfeedback',
            unique_together=set([('adjudicator', 'source_adjudicator', 'source_team', 'version')]),
        ),
    ]