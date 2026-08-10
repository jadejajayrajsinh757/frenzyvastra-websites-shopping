from django.views.generic import TemplateView
from django.http import HttpResponse



def show_jarvis(request):
    return HttpResponse("Jarvis is running")


class AboutPageView(TemplateView):
    template_name = "about.html"


class MensPageView(TemplateView):
    template_name = "mens.html"
