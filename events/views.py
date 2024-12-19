from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Event
from .form import form_class
from events import models

# 表示するやつ


def index(request):
    context = {}
    return render(request, "apps/index.html", context)


def create(request):
    title = request.POST.get("title")
    new_event = models.Event()
    new_event.event_title = title
    new_event.save()
    return HttpResponseRedirect(reverse("event:index"))
