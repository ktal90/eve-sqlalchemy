# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from eve_sqlalchemy.examples.many_to_many import settings
from eve_sqlalchemy.examples.many_to_many.domain import Base
from eve_sqlalchemy.tests import TestMinimal

SETTINGS = vars(settings)


class TestManyToMany(TestMinimal):

    def setUp(self, url_converters=None):
        super(TestManyToMany, self).setUp(SETTINGS, url_converters, Base)

    def bulk_insert(self):
        self.app.data.insert('children', [{'id': k} for k in range(1, 5)])
        self.app.data.insert('parents', [
            {'id': 1, 'children': [1, 2]},
            {'id': 2, 'children': [1, 3]},
            {'id': 3, 'children': []}])

    def test_get_related_children_with_where(self):
        response, status = self.get('children', '?where={"parents": 1}')
        self.assert200(status)
        children = response['_items']
        self.assertEqual([c['id'] for c in children], [1, 2])

    def test_get_related_parents_with_where(self):
        response, status = self.get('parents', '?where={"children": 1}')
        self.assert200(status)
        parents = response['_items']
        self.assertEqual([p['id'] for p in parents], [1, 2])
