# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Parpol
from .models import Person
from .models import Terpilih

# Create your views here.

def index(request):
    parpol = Parpol.objects.order_by('id')[:5]
    context = { 'parpols': parpol }
    return render(request, 'index.html', context)

def show(request, choice):
    parpol_usungan = get_object_or_404(Parpol, pk=choice)
    context = {'parpol_usungan':parpol_usungan}
    return render(request, 'show.html', context)