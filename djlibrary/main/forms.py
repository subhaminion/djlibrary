from django.forms import ModelForm
from main.models import Author, Book


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'email']


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publication_date']