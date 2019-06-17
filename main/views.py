from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from main.models import Messages



def create(request):
    if request.method == "POST":
        new_message = Messages()
        new_message.textMessage = request.POST.get("textMessage")
        if new_message.textMessage != '':
            new_message.save()
    return HttpResponseRedirect("/")