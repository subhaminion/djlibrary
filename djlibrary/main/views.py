from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Author, Book
from main.forms import AuthorForm, BookForm


def index(request, template_name="index.html"):
    author = Author.objects.all()
    data = {}
    data['object_list'] = author
    return render(request, template_name, data)


def author_create(request, template_name="post_author.html"):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def book_create(request, template_name="post_book.html"):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def book_list(request, pk, template_name="book_list.html"):
    author = get_object_or_404(Author, pk=pk)
    books = author.book_set.all()
    data = {}
    data['object_list'] = books
    return render(request, template_name, data)
