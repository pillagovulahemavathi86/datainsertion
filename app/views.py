from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic inserted sucessfully')

def insert_webpage(request):
    tn=input('enter a topic')
    n=input('enter name')
    url=input('enter a url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    
    return HttpResponse('webpage inserted successfully')

def insert_accessrecords(request):
    tn=input('enter topic name')
    n=input('enter a name')
    url=input('enter url')
    a=input('enter author')
    d=input('enter date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    AO=Accessrecords.objects.get_or_create(name=WO,author=a,date=d)[0]
    AO.save()
    return HttpResponse('inserted access record successfully')


    