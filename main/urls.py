from django.conf.urls import url
from django.urls import path
from django.views.generic import ListView
from main.models import Messages
from main.views import create


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Messages.objects.all(), template_name="mainPage.html")),
    path('create', create)
]