"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('employee/add/', views.employee_add_view, name="employee_add_view"),
    path('employee/<int:employee_id>/', views.employee_detail_view, name="employee_detail_view"),
    path('employee/<int:employee_id>/edit/', views.employee_edit_view, name="employee_edit_view"),
    path('ticket/add/', views.ticket_add_view),
    path('ticket/<int:ticket_id>/', views.ticket_detail_view, name="ticket_detail_view"),
    path('ticket/<int:ticket_id>/edit', views.ticket_edit_view),
    path('ticket/<int:ticket_id>/assign', views.ticket_assign_view),
    path('ticket/<int:ticket_id>/done', views.ticket_done_view),
    path('ticket/<int:ticket_id>/invalid', views.ticket_invalid_view),
    path('ticket/<int:ticket_id>/reopen', views.ticket_reopen_view),
    path('ticket/<int:ticket_id>/return', views.ticket_return_view),
]
