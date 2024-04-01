from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def index(request):
    # HTML page as a string
    template =  "<html>" \
                "This is your first view!" \
                "</html>"
    # return the template as the content argument in HTTP response
    return HttpResponse(content=template)
  
def get_date(request):
    # store the date
    today = date.today()
    # HTML page with date as a string
    template =  "<html>" \
                "Today's date is {}" \
                "</html>".format(today)
    # return the template object
    return HttpResponse(content=template)
    
