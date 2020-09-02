from django.db import models
from core.models import AbstractTimeStamp


class Category(AbstractTimeStamp):
    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"
    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )

    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=6, choices=KIND_CHOICES, default=KIND_BOOK)
