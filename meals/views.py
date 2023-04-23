from django.shortcuts import render
from .models import Meals


# Create your views here.


def media_list(request):

    meal_list = Meals.objects.all()

    context = {'meal_list': meal_list, }

    return render(request, 'Meals/list.html', context)


def meal_detail(request, slug):
    pass
