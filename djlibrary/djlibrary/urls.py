from django.conf.urls import url, include
from django.contrib import admin
from main.views import (
    index, author_create, book_create
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'books', index, name='index'),
    url(r'author_create', author_create, name='author_create'),
    url(r'book_create', book_create, name='book_create'),
]
