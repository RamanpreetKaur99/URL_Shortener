from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# Create your views here.

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import KirrURL
from . import models
# def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
#    obj = get_object_or_404(KirrURL, shortcode =shortcode)
#    return HttpResponseRedirect(obj.url)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context ={
            "title" : "URL SHORTENER",
            "form" : the_form
        }
        return render(request, "shortener/home.html",context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context ={
            "title" : "URL SHORTENER",
            "form" : form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object" : obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template,context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        ''' obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)  '''

        obj = models.KirrURL.objects.get(shortcode=shortcode)
        real_link = obj.url
        return redirect(real_link)



#    def post(self, request, *args, **kwargs):
#        return HttpResponse()
