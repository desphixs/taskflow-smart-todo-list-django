# We import render, get_object_or_404, and redirect to handle template compilation, safe object lookups, and routing.
# Think of redirect like an "Airport Transfer Chauffeur Portal": once a customer finishes a specific step,
# the chauffeur securely picks them up, guides them out of the current page terminal, and drops them off
# at another active page gate (e.g. the home dashboard list) seamlessly!
from django.shortcuts import render, get_object_or_404, redirect
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


# Our create_task view handles processing submitted task inputs and saving them directly into our SQLite database.
# Think of this view like a secure database registrar: when a student fills out a registration form,
# the registrar inspects the document, logs it cleanly inside the master register cabinet,
# and then immediately guides them back to the active list view dashboard!
def create_task(request):
    # We check if the incoming request type is 'POST' (which means someone submitted form input data).
    # Think of a POST request like sending a locked secure mail courier package back to the office kitchen!
    if request.method == 'POST':
        # We extract the string value typed inside the form field labeled exactly name='title'.
        # Think of this like pulling the typed letter out of the secure mail envelope!
        title = request.POST.get('title')
        
        # We confirm that the user actually typed some characters to prevent registering blank tasks!
        if title:
            # We use our ORM model manager 'objects.create' to save this task straight into a new SQLite database row!
            # Think of this like registering a brand new folder containing the given title inside our Tasks drawer!
            Task.objects.create(title=title)
            
    # Once the task is saved (or if the request is not a POST), we call the redirect function.
    # This guides the visitor back to our main home dashboard list view route, updating the board in real-time!
    return redirect('tasks:task_list')
