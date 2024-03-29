from django.urls import reverse
from django.db import models
from core.models import AbstractTimeStamp


class Person(AbstractTimeStamp):
    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"

    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=120)
    photo = models.ImageField(null=True, blank=True)
    kind = models.CharField(max_length=15, choices=KIND_CHOICES)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("people:people_detail", kwargs={"pk": self.pk})