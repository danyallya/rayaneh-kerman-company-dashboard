from django.contrib import admin

from pm.models import TimeSpend, Project
from utils.admin import HardModelAdmin

admin.site.register(TimeSpend, HardModelAdmin)

admin.site.register(Project, HardModelAdmin)
