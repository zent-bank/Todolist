from functools import total_ordering
from django.contrib import admin
from .models import Todolist

admin.site.register(Todolist)