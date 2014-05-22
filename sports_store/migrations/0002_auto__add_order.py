# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'sports_store_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('giftwrap', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sports_store', ['Order'])

        # Adding M2M table for field products on 'Order'
        m2m_table_name = db.shorten_name(u'sports_store_order_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm[u'sports_store.order'], null=False)),
            ('product', models.ForeignKey(orm[u'sports_store.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['order_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'sports_store_order')

        # Removing M2M table for field products on 'Order'
        db.delete_table(db.shorten_name(u'sports_store_order_products'))


    models = {
        u'sports_store.order': {
            'Meta': {'object_name': 'Order'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'giftwrap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sports_store.Product']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'sports_store.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        }
    }

    complete_apps = ['sports_store']