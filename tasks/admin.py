from django.contrib import admin
# We import the Task model from our local models.py file in the current directory.
# The single dot '.' means "look in my current folder where this file sits"!
from .models import Task

# Register your models here.
# Think of the Django Admin Panel as a secure, high-tech control center dashboard.
# By registering our model here, we are mounting a dashboard monitor screen for our filing cabinets!
# It gives authorized store managers (Admins) a premium visual dashboard to view, add, search, and delete tasks.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # The list_display option defines which drawers (columns) of our filing cabinets are visible on the dashboard monitor.
    # Think of this like choosing what data columns are displayed in a clean spreadsheet!
    # Instead of only showing the title, we want to see if the task is completed and the exact date it was created.
    list_display = (
        'title',          # Show the task description column
        'is_completed',   # Show the completion status checkbox column
        'created_at'      # Show the smart date and time stamp column
    )

    # The list_filter option mounts a "Smart Filtering Panel" on the right side of the dashboard.
    # Think of this like shopping online and clicking a filter option to only see green shirts!
    # With this, admins can easily toggle their view to show only completed tasks or active ones with one click.
    list_filter = (
        'is_completed',   # Allow filtering list items by completed/active states
        'created_at'      # Allow filtering list items by creation dates
    )

    # The search_fields option places a "Search Bar Input Field" at the very top of our dashboard list.
    # Think of this like a search bar in an email inbox.
    # When an admin types a word, Django scans the 'title' column to instantly find matching tasks!
    search_fields = (
        'title',          # Enable searching tasks by their text titles
    )

    # The date_hierarchy option adds a "Time Travel Navigator Bar" at the very top of our listing.
    # Think of this like a chronological timeline slider.
    # It allows managers to drill down and explore tasks by years, months, or days!
    date_hierarchy = 'created_at'
