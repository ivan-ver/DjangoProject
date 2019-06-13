from django.http import HttpResponse, HttpResponseRedirect
from main.models import Messages



def create(request):
    if request.method == "POST":
        new_message = Messages()
        new_message.textMessage = request.POST.get("textMessage")
        new_message.save()
    return HttpResponseRedirect("/")
