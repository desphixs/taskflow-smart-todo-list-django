from django.db import models

# Create your models here.
# Think of a Database Model as a blueprint for building physical filing cabinets in our office.
# In a business, you don't just dump all papers on the floor! Instead, you build a custom filing cabinet (a Table)
# and define exactly what drawers it has (Fields) and what kind of files are allowed to go into each drawer (Data Types).
# In Django, a Model is a special Python class that acts as the blueprint for these filing cabinets!
class Task(models.Model):
    # The title represents our first filing cabinet drawer.
    # Think of CharField like a "Text Label Drawer" where you write down short task names.
    # We restrict its size using max_length=200, which acts like a physical label strip that can only fit 200 letters!
    title = models.CharField(
        max_length=200,
        verbose_name="Task Title",
        help_text="Enter the description or title of the task you want to complete."
    )

    # The is_completed field represents our second filing cabinet drawer.
    # Think of BooleanField like a "Checkbox Toggle Switch" drawer.
    # It can only be turned ON (True) or OFF (False). We set default=False because when a user
    # creates a brand-new task, they haven't completed it yet!
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Is Completed?",
        help_text="Check this box if the task has been fully completed."
    )

    # The created_at field represents our third filing cabinet drawer.
    # Think of DateTimeField with auto_now_add=True like a "Smart Date Stamp Machine".
    # Every time you drop a new paper sheet (a new task row) into the cabinet, the smart machine
    # automatically stamps the exact current time and date onto it, so you never have to type it by hand!
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The exact date and time this task was registered on the board."
    )

    # The __str__ method is a special magic Python function.
    # Think of this like printing a clear sticky label card and sticking it to the front of a physical folder.
    # By default, if you don't define this, the computer just shows an ugly barcode ID number (like 'Task object (1)').
    # By returning the task title, we tell Django: "When showing this task in lists, print its human-readable title!"
    def __str__(self):
        # We return the string representation of our task, which is its title.
        return self.title

    # The Meta subclass allows us to define extra hidden rules for our filing cabinets.
    # Think of this like writing organization guidelines on the inside cover of the binder!
    class Meta:
        # We use ordering = ['-created_at'] to tell Django to organize our folders.
        # The minus '-' symbol means "descending order" (newest first).
        # This acts like a smart tray that automatically keeps the newest papers right at the very top of the pile!
        ordering = ['-created_at']
        # We define a friendly name for a single task row.
        verbose_name = "Task"
        # We define a friendly name for plural lists of task rows.
        verbose_name_plural = "Tasks"
