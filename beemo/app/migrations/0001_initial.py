# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Coach'
        db.create_table(u'app_coach', (
            ('cid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'app', ['Coach'])

        # Adding model 'Clinic'
        db.create_table(u'app_clinic', (
            ('vid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('cid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'app', ['Clinic'])

        # Adding model 'Participant'
        db.create_table(u'app_participant', (
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=60, primary_key=True)),
            ('coach', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='participants', null=True, to=orm['app.Coach'])),
            ('clinic', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='participants', null=True, to=orm['app.Clinic'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('fat_goal', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fruit_goal', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('veg_goal', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fiber_goal', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('step_goal', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('nc_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Participant'])

        # Adding model 'Call'
        db.create_table(u'app_call', (
            ('cid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='calls', to=orm['app.Participant'])),
            ('coach', self.gf('django.db.models.fields.related.ForeignKey')(related_name='calls', to=orm['app.Coach'])),
            ('scheduled_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('completed_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('fat_goal', self.gf('django.db.models.fields.TextField')()),
            ('fruit_goal', self.gf('django.db.models.fields.TextField')()),
            ('veg_goal', self.gf('django.db.models.fields.TextField')()),
            ('fiber_goal', self.gf('django.db.models.fields.TextField')()),
            ('step_goal', self.gf('django.db.models.fields.TextField')()),
            ('call_note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'app', ['Call'])

        # Adding model 'ParticipantNote'
        db.create_table(u'app_participantnote', (
            ('pid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='p_notes', to=orm['app.Participant'])),
            ('coach', self.gf('django.db.models.fields.related.ForeignKey')(related_name='p_notes', to=orm['app.Coach'])),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'app', ['ParticipantNote'])

        # Adding model 'ParticipantProblem'
        db.create_table(u'app_participantproblem', (
            ('pid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='problems', to=orm['app.Participant'])),
            ('problem', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'app', ['ParticipantProblem'])


    def backwards(self, orm):
        # Deleting model 'Coach'
        db.delete_table(u'app_coach')

        # Deleting model 'Clinic'
        db.delete_table(u'app_clinic')

        # Deleting model 'Participant'
        db.delete_table(u'app_participant')

        # Deleting model 'Call'
        db.delete_table(u'app_call')

        # Deleting model 'ParticipantNote'
        db.delete_table(u'app_participantnote')

        # Deleting model 'ParticipantProblem'
        db.delete_table(u'app_participantproblem')


    models = {
        u'app.call': {
            'Meta': {'object_name': 'Call'},
            'call_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'calls'", 'to': u"orm['app.Coach']"}),
            'completed_date': ('django.db.models.fields.DateTimeField', [], {}),
            'fat_goal': ('django.db.models.fields.TextField', [], {}),
            'fiber_goal': ('django.db.models.fields.TextField', [], {}),
            'fruit_goal': ('django.db.models.fields.TextField', [], {}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'calls'", 'to': u"orm['app.Participant']"}),
            'scheduled_date': ('django.db.models.fields.DateTimeField', [], {}),
            'step_goal': ('django.db.models.fields.TextField', [], {}),
            'veg_goal': ('django.db.models.fields.TextField', [], {})
        },
        u'app.clinic': {
            'Meta': {'object_name': 'Clinic'},
            'cid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'app.coach': {
            'Meta': {'object_name': 'Coach'},
            'cid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'app.participant': {
            'Meta': {'object_name': 'Participant'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'clinic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'participants'", 'null': 'True', 'to': u"orm['app.Clinic']"}),
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'participants'", 'null': 'True', 'to': u"orm['app.Coach']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'fat_goal': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fiber_goal': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fruit_goal': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'nc_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '60', 'primary_key': 'True'}),
            'step_goal': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'veg_goal': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.participantnote': {
            'Meta': {'object_name': 'ParticipantNote'},
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'p_notes'", 'to': u"orm['app.Coach']"}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'p_notes'", 'to': u"orm['app.Participant']"}),
            'pid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'app.participantproblem': {
            'Meta': {'object_name': 'ParticipantProblem'},
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'problems'", 'to': u"orm['app.Participant']"}),
            'pid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'problem': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['app']