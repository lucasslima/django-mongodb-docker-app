from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Sugestion,SugestionForm

def sugestions(request):
    if request.method == 'GET':
        form = SugestionForm()
    else:
        form = SugestionForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            return redirect('success/')
    return render(request, "sugestions.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
