from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Employee
from tickets.models import Ticket

# Register your models here.
UserAdmin.fieldsets[1][1]['fields'] += ('displayname', 'avatar', 'position')

admin.site.register(Employee, UserAdmin)
admin.site.register(Ticket)
