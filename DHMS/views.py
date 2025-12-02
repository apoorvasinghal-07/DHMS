from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

    title = {'title': 'Apporva | Home'}
    return render(request,'index.html',title)

def about(request):

    title = {'title': 'Apporva | about'}
    return render(request,'About.html',title)

def blog(request):

    title = {'title': 'Apporva | blog'}
    return render(request,'Blog.html',title)

def Contact(request):

    title = {'title': 'Apporva | Contact'}
    return render(request,'contact.html',title)

def Feature(request):

    title = {'title': 'Apporva | Feature'}
    return render(request,'feature.html',title)

def Service(request):

    title = {'title': 'Apporva | Service'}
    return render(request,'service.html',title)

def Appointment(request):

    title = {'title': 'Apporva | Appointment'}
    return render(request,'appointment.html',title)