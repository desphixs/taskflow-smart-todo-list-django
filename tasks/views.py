# We import get_object_or_404 alongside render to securely retrieve database objects.
# Think of get_object_or_404 like a friendly archivist butler: when we ask him to pull a document with ID 5,
# if it exists, he grabs it cleanly. If it's missing, he turns around and politely says "404: Not Found",
# preventing our Python server from crashing due to a missing folder!
from django.shortcuts import render, get_object_or_404
# We import HttpResponse to demonstrate how to send a raw text/HTML response directly back to the browser.
# In professional web apps, returning raw text or writing full HTML inside Python strings is incredibly messy!
# That is why we quickly graduate to using the 'render' function, which loads a separate, clean HTML template.
from django.http import HttpResponse

# We import our Task database model class so we can fetch real tasks from the SQLite database.
# The single dot '.' in '.models' tells Python to look in our current 'tasks' application folder!
from .models import Task

# Create your views here.
# In Django, a "view" is just a standard Python function that takes a web request and returns a web response.
# Think of a view function like a friendly restaurant chef: when a customer submits an order (a web request),
# the chef prepares the meal (processes the request) and sends the finished plate back (the response)!
def task_list(request):
    # Instead of using hardcoded mock lists (which act like writing fake menu items directly on a piece of paper),
    # we now use Django's ORM (Object-Relational Mapper) to query our physical database!
    # Think of 'Task.objects.all()' like telling a store manager: "Go over to our active database filing cabinet,
    # open the drawer labeled 'Tasks', and fetch every single record folder sitting in there!"
    # Since we configured the Meta class in models.py to sort by '-created_at', Django automatically organizes
    # these records so the newest tasks are at the top of the pile!
    tasks = Task.objects.all()

    # We pack our fetched database records list inside a central Python dictionary called 'context'.
    # Think of the context dictionary like a server carrying a covered tray of dishes to a dining table:
    # the tray (context) holds specific labels ('tasks') so the template knows exactly how to identify
    # the correct dish once the cover is lifted!
    context = {
        'tasks': tasks,
    }

    # The 'render' function takes the context dictionary as its third argument.
    # This delivers our packed database records straight to the templates/tasks/index.html file so it can be dynamically compiled!
    return render(request, 'tasks/index.html', context)


# Our dynamic task_detail view handles displaying complete details for one specific task.
# Think of this view function like a highly focused researcher: when someone asks for details on a specific project,
# the researcher goes straight to the filing catalog, extracts the single correct folder, and loads it for display!
def task_detail(request, pk):
    # We fetch a single specific Task record from our database using its unique Primary Key (pk).
    # Think of this like entering a physical document archive room: you tell the archivist:
    # "Please pull out the folder labeled exactly with ID number 5!"
    # The 'get_object_or_404' helper uses Task.objects.get(pk=pk) behind the scenes.
    # If the folder exists, it is loaded. If it's empty or missing, Django automatically triggers a 404 page,
    # preventing server crashes and letting the visitor know the document doesn't exist!
    task = get_object_or_404(Task, pk=pk)

    # We pack our loaded task folder onto a context dictionary catering tray under the label 'task'.
    # The template can now lift this label cover to extract the task's individual details (title, completion, date)!
    context = {
        'task': task,
    }

    # We render and deliver the loaded task detail template back to the browser screen.
    return render(request, 'tasks/task_detail.html', context)
