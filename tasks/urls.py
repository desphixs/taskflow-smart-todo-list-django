# We import path from django.urls to define our app's specific route mappings.
from django.urls import path
# We import the views file from our current directory (represented by the dot '.') to access our view functions.
from . import views

# We define a variable called 'app_name' to namespace our routes.
# Think of this like giving our tasks storefront its own unique brand name prefix: it prevents Django
# from getting confused if another app in our shopping mall project has a route with the exact same name!
app_name = 'tasks'

# The urlpatterns list holds all the active routes that belong specifically to our tasks app.
# Think of this list like a specialized navigation signpost mounted right inside the tasks department itself!
urlpatterns = [
    # This empty path '' maps directly to the root address of the tasks storefront.
    # When a visitor lands here, Django will call the 'task_list' view function (our chef) in views.py!
    # We assign name='task_list' so we can easily generate dynamic URL links in our templates later.
    path('', views.task_list, name='task_list'),

    # This dynamic path '<int:pk>/' maps requests to an individual task's details page.
    # Think of '<int:pk>' like a "Dynamic Postbox Number Selector".
    # Instead of making 100 separate static URL links for 100 tasks, we write a single dynamic stencil route!
    # Django matches any integer entered in this position (e.g. /tasks/5/), extracts that number,
    # stores it under the variable name 'pk' (Primary Key), and hands it over to our 'task_detail' view function!
    # We assign name='task_detail' to easily link task titles straight to their pages using {% url 'tasks:task_detail' task.id %}.
    path('<int:pk>/', views.task_detail, name='task_detail'),

    # This route maps to our secure task creation view function.
    # When our HTML index page submits form details via POST, it sends the parameters to /create/!
    # The view processes the details and redirects the user right back to the homepage list.
    path('create/', views.create_task, name='create_task'),

    # This dynamic route handles toggling completion states back and forth.
    # When a user clicks our form checkbox, it triggers a POST call to /<id>/toggle/, flipping state!
    path('<int:pk>/toggle/', views.toggle_task, name='toggle_task'),
]
