from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from movies.models import Movie
from books.models import Book
from people.models import Person


def resolve_home(request):
    movies = Movie.objects.all().order_by("pk")[:10]
    books = Book.objects.all().order_by("pk")[:10]
    people = Person.objects.all().order_by("pk")[:10]

    return render(
        request,
        "home.html",
        {
            "movies": movies,
            "books": books,
            "people": people,
            "page_title": "Home",
        },
    )


def resolve_search(request):
    return render(
        request,
        "search.html",
        {
            "page_title": "Search",
        },
    )
