from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def elements_view(request):
    return render(request, 'website/elements.html')


def contact_view(request):
    return render(request, 'website/contact.html')


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form. is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
