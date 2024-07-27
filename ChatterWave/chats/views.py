from django.shortcuts import render

def messages_page(request):
    render(request,"messages.html")