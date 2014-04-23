# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'gallery_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'gallery', ['Item'])

        # Adding model 'Photo'
        db.create_table(u'gallery_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Item'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'gallery', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'gallery_item')

        # Deleting model 'Photo'
        db.delete_table(u'gallery_photo')


    models = {
        u'gallery.item': {
            'Meta': {'ordering': "['name']", 'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'gallery.photo': {
            'Meta': {'ordering': "['title']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Item']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['gallery']