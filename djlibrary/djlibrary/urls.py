from django.conf.urls import url, include
from django.contrib import admin
from main.views import (
    index, author_create, book_create,
    book_list
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index', index, name='index'),
    url(r'author_create', author_create, name='author_create'),
    url(r'book_create', book_create, name='book_create'),
    url(r'book_list/(?P<pk>\d+)$', book_list, name='book_list'),
]
