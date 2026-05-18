"""
URL configuration for taskflow_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# We import path and include from django.urls to define routes and connect sub-routing files.
# Think of 'path' like a signpost at a physical crossroad, and 'include' like a master directory operator
# that forwards visitors straight to our tasks app's own internal signpost directory list!
from django.urls import path, include

# The urlpatterns list holds all the active routes for our website.
# Think of this list like a master directory at the entrance of a shopping mall.
# It matches what the user typed in the browser's address bar to the correct department!
urlpatterns = [
    # This route maps the path 'admin/' to Django's built-in administrator site.
    # When a user goes to http://127.0.0.1:8000/admin, this entry sends them to the admin portal.
    path('admin/', admin.site.urls),

    # We include our tasks app's URLs at the empty root path of our website!
    # When a visitor goes to the base URL http://127.0.0.1:8000/, this entry forwards
    # them directly to the internal tasks/urls.py file to find the correct view function!
    path('', include('tasks.urls')),
]

