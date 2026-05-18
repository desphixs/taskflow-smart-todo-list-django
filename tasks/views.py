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
    # In a fully-fledged database application, we would retrieve tasks out of physical database tables.
    # For now, we define a list of standard Python dictionaries representing our tasks.
    # Think of this list like a physical clipboard list of paper sheets: each sheet (dictionary) has a
    # task name ('title'), a marker checkmark ('completed') indicating if it's done or pending,
    # and a label ('created_at') telling us when the task was added.
    tasks = [
        {
            'title': 'Set up virtual environment and Django project',
            'completed': True,
            'created_at': 'just now'
        },
        {
            'title': 'Build the tasks board view and templates',
            'completed': False,
            'created_at': 'today'
        },
        {
            'title': 'Design sticky note task grid mockup',
            'completed': True,
            'created_at': 'yesterday'
        },
    ]

    # We pack our list inside a central Python dictionary called 'context'.
    # Think of the context dictionary like a server carrying a covered tray of dishes to a dining table:
    # the tray (context) holds specific labels ('tasks') so the template knows exactly how to identify
    # the correct dish once the cover is lifted!
    context = {
        'tasks': tasks,
    }

    # The 'render' function takes the context dictionary as its third argument.
    # This delivers our packed data straight to the templates/tasks/index.html file so it can be dynamically compiled!
    return render(request, 'tasks/index.html', context)
