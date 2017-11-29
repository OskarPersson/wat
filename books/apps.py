# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class BooksConfig(AppConfig):
    name = 'books'

    def ready(self):
        Book = self.get_model("Book")
        watson.register(Book, fields=('title',))
