# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestCase'
        db.create_table(u'courses_testcase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Task'])),
        ))
        db.send_create_signal(u'courses', ['TestCase'])

        # Adding model 'ScoreProfile'
        db.create_table(u'courses_scoreprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('current_rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Ranking'])),
            ('score', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'courses', ['ScoreProfile'])

        # Adding model 'Task'
        db.create_table(u'courses_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('points_reward', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'courses', ['Task'])

        # Adding model 'CompilerProfile'
        db.create_table(u'courses_compilerprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compile_cmd', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('execute_cmd', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'courses', ['CompilerProfile'])

        # Adding model 'Ranking'
        db.create_table(u'courses_ranking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('required_score', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'courses', ['Ranking'])


    def backwards(self, orm):
        # Deleting model 'TestCase'
        db.delete_table(u'courses_testcase')

        # Deleting model 'ScoreProfile'
        db.delete_table(u'courses_scoreprofile')

        # Deleting model 'Task'
        db.delete_table(u'courses_task')

        # Deleting model 'CompilerProfile'
        db.delete_table(u'courses_compilerprofile')

        # Deleting model 'Ranking'
        db.delete_table(u'courses_ranking')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courses.compilerprofile': {
            'Meta': {'object_name': 'CompilerProfile'},
            'compile_cmd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'execute_cmd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'courses.course': {
            'Meta': {'object_name': 'Course'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'registration_end': ('django.db.models.fields.DateTimeField', [], {}),
            'registration_limit': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'registration_start': ('django.db.models.fields.DateTimeField', [], {}),
            'registrations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'through': u"orm['courses.Registration']", 'symmetrical': 'False'})
        },
        u'courses.ranking': {
            'Meta': {'object_name': 'Ranking'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'required_score': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'courses.registration': {
            'Meta': {'object_name': 'Registration'},
            'code_master': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            'granted': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'courses.scoreprofile': {
            'Meta': {'object_name': 'ScoreProfile'},
            'current_rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Ranking']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'courses.task': {
            'Meta': {'object_name': 'Task'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points_reward': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courses.testcase': {
            'Meta': {'object_name': 'TestCase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Task']"})
        }
    }

    complete_apps = ['courses']