"""ask_movsesov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<page>\d+)$', views.index, name='page'),
    url(r'^question/(?P<question_id>\d+)$', views.get_question, name='get_question'),
    url(r'^makePost/(?P<question_id>\d+)', views.makeAnswer, name='makePost'),
    url(r'^tag/(?P<tag_id>\d+)', views.list_by_tag, name='by_tag'),
    url(r'^tag/(?P<tag_id>\d+)/page/(?P<page>\d+)', views.list_by_tag, name='page'),
]