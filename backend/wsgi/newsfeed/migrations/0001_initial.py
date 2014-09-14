# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsItem'
        db.create_table(u'newsfeed_newsitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('intro', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('tinymce.models.HTMLField')()),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'newsfeed', ['NewsItem'])


    def backwards(self, orm):
        # Deleting model 'NewsItem'
        db.delete_table(u'newsfeed_newsitem')


    models = {
        u'newsfeed.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'body': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['newsfeed']