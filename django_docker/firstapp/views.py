from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # HTML page as a string
    template =  "<html>" \
                "This is your first view!" \
                "</html>"
    # return the template as the content argument in HTTP response
    return HttpResponse(content=template)
  
