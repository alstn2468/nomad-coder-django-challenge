from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.http import Http404
from django.shortcuts import redirect, reverse
from books.models import Book


class BookListView(ListView):
    model = Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "books"

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(BookListView, self).dispatch(request, *args, **kwargs)

        except Http404:
            return redirect(reverse("core:home"))


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = [
        "title",
        "year",
        "cover_image",
        "category",
        "writer",
        "rating",
    ]


class BookUpdateView(UpdateView):
    model = Book
    fields = [
        "title",
        "year",
        "cover_image",
        "category",
        "writer",
        "rating",
    ]
