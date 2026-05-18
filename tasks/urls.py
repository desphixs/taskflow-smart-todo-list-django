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
]
