from django.shortcuts import render
# We import HttpResponse to demonstrate how to send a raw text/HTML response directly back to the browser.
# In professional web apps, returning raw text or writing full HTML inside Python strings is incredibly messy!
# That is why we quickly graduate to using the 'render' function, which loads a separate, clean HTML template.
from django.http import HttpResponse

# Create your views here.
# In Django, a "view" is just a standard Python function that takes a web request and returns a web response.
# Think of a view function like a friendly restaurant chef: when a customer submits an order (a web request),
# the chef prepares the meal (processes the request) and sends the finished plate back (the response)!
def task_list(request):
    # Below is how we would return a simple raw string using HttpResponse:
    # return HttpResponse("Welcome to TaskFlow! Your task-tracking journey starts here.")
    #
    # However, to keep our codebase professional and easy to style, we will render our separate HTML template.
    # The 'render' function tells Django: "Go find the HTML file named 'tasks/index.html' inside the templates folder,
    # package it up, and deliver it as a completed web response to the user's screen!"
    # The first argument is the incoming request object, and the second is our template path.
    return render(request, 'tasks/index.html')
