from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpRequest , HttpResponse
from typing import Any
from .models import Shoes



class HomeListView(ListView):
    template_name = 'index.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        shoes = Shoes.objects.all()

        context = {
            'shoes':shoes,
        }

        return render(request , self.template_name, context=context)






