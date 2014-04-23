# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Photo.image'
        db.alter_column(u'gallery_photo', 'image', self.gf('gallery.items.fields.ThumbnailImageField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Photo.image'
        db.alter_column(u'gallery_photo', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

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
            'image': ('gallery.items.fields.ThumbnailImageField', [], {'max_length': '100'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Item']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['gallery']