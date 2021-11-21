"""account_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.shortcuts import render

import logging


class CheckForm(forms.Form):
    mycheckbox = forms.BooleanField(required=False)


logger = logging.getLogger(__name__)


def my_view(request):
    logger.info('Testing condition')
    logger.warning('Something bad happened')
    return HttpResponse(200)


def other_view(request, parameter):
    print(request.method)
    logger.warning(f'Other view {parameter} {type(parameter)}')
    if request.method == 'POST':
        logger.warning(f'POST {request.POST}')
    logger.warning(f'{request.method}')
    return HttpResponse(200)


def third_view(request, parameter):
    logger.warning(f'Other third view {parameter} {type(parameter)}')
    return HttpResponse(200)


def form_view(request):
    form = CheckForm()
    if request.method == 'POST':
        logger.warning(f'POST {request.POST}')

    if request.method == 'GET':
        logger.warning(f'GET {request.GET}')
        logger.warning(f'{request.GET["param1"]}')
        logger.warning(f'{request.GET["param2"]}')
        logger.warning(f'{request.GET.getlist("param1")}')
        logger.warning(f'{request.headers}')
        logger.warning(f'{request.META}')

    return render(request, 'form.html', {'form': form})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', form_view),
    path('something/', my_view),
    path('something/<int:parameter>', other_view),
    path('something/<str:parameter>', third_view),
]
