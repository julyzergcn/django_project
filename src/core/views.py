from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render

from . import models


def homepage(request):
    return render(request, 'homepage.html')
