from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from users.models import Employee
from users.forms import EmployeeForm, LoginForm
from tickets.models import Ticket
from tickets.forms import TicketAddForm

# Create your views here.
@login_required
def index(request):
    new_tickets = Ticket.objects.filter(status='New').order_by('-date_filed')
    in_progress_tickets = Ticket.objects.filter(status='In Progress').order_by('-date_filed')
    completed_tickets = Ticket.objects.filter(status='Done').order_by('-date_filed')
    invalid_tickets = Ticket.objects.filter(status="Invalid").order_by('-date_filed')
    all_tickets = [
        {'header': 'New Tickets', 'tickets': new_tickets},
        {'header': 'In Progress Tickets', 'tickets': in_progress_tickets},
        {'header': 'Completed Tickets', 'tickets': completed_tickets},
        {'header': 'Invalid Tickets', 'tickets': invalid_tickets},
    ]

    return render(request, 'index.html',{'all_tickets': all_tickets})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, "generic_form.html", {'form': form, 'header': 'Staff Login', 'button_value': 'Login'})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def employee_add_view(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_employee = Employee.objects.create_user(
                username=data['username'],
                password = data['password'],
                displayname = data['displayname'],
                avatar = data['avatar'],
                position = data['position'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email']
                )
            return HttpResponseRedirect(reverse('employee_detail_view', args=(new_employee.id,)))
    
    form = EmployeeForm()
    return render(request, 'generic_form.html', {
        'form': form,
        'header': 'Create New Employee Account',
        'button_value': 'Create New Employee'
        })


@login_required
def employee_edit_view(request, employee_id: int):
    if request.user.id != employee_id:
        return render(request, 'employee_edit_restricted.html')

    employee = Employee.objects.get(id=employee_id)

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            employee.username=data['username']
            employee.displayname = data['displayname']
            employee.set_password(data['password'])
            employee.avatar = data['avatar']
            employee.position = data['position']
            employee.first_name = data['first_name']
            employee.last_name = data['last_name']
            employee.email = data['email']
            employee.save()
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse('employee_detail_view', args=(employee_id,)))
    
    form = EmployeeForm(initial={
        'username': employee.username,
        'displayname': employee.displayname,
        'avatar': employee.avatar,
        'position': employee.position,
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'email': employee.email,
    })

    return render(request, 'generic_form.html', {
        'form': form,
        'header': 'Edit Employee Profile',
        'button_value': 'Save'
        })


@login_required
def employee_detail_view(request, employee_id: int):
    employee = Employee.objects.get(id=employee_id)
    filed_tickets = Ticket.objects.filter(creator=employee).order_by('-date_filed')
    in_progress_tickets = Ticket.objects.filter(assigned_to=employee).order_by('-date_filed')
    completed_tickets = Ticket.objects.filter(completed_by=employee).order_by('-date_filed')
    all_tickets = [
        {'header': 'Filed Tickets', 'tickets': filed_tickets},
        {'header': 'In Progress Tickets', 'tickets': in_progress_tickets},
        {'header': 'Completed Tickets', 'tickets': completed_tickets},
    ]
    return render(request, 'employee_detail.html',{
        'employee': employee,
        'all_tickets': all_tickets,
        })


@login_required
def ticket_add_view(request):
    if request.method == "POST":
        form = TicketAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = Ticket.objects.create(
                title = data['title'],
                description = data['description'],
                creator = request.user
            )
            return HttpResponseRedirect(reverse('ticket_detail_view', args=(new_ticket.id,)))
    
    form = TicketAddForm()
    return render(request, 'generic_form.html', {'form': form, 'header': 'Submit a Ticket', 'button_value': "Submit"})


@login_required
def ticket_edit_view(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        form = TicketAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()

            return HttpResponseRedirect(reverse('ticket_detail_view', args=(ticket_id,)))
    
    form = TicketAddForm(initial={
        'title': ticket.title,
        'description': ticket.description
    })
    return render(request, 'generic_form.html', {'form': form, 'header': 'Edit Ticket', 'button_value': 'Save'})

@login_required
def ticket_detail_view(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    current_user = request.user
    return_btn = False
    if ticket.assigned_to == current_user:
        return_btn = True
    return render(request, 'ticket_detail.html', {'ticket': ticket, 'current_user': current_user, 'return_btn': return_btn})


@login_required
def ticket_assign_view(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = "In Progress"
    ticket.assigned_to = request.user
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_view', args=(ticket_id,)))


@login_required
def ticket_done_view(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = "Done"
    ticket.completed_by = request.user
    ticket.assigned_to = None
    ticket.completed_before = True
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_view', args=(ticket_id,)))


@login_required
def ticket_invalid_view(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = "Invalid"
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_view', args=(ticket_id,)))


@login_required
def ticket_reopen_view(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = "In Progress"
    ticket.assigned_to = request.user
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_view', args=(ticket_id,)))


@login_required
def ticket_return_view(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    if ticket.completed_before:
        ticket.status = "In Progress"
    else:
        ticket.status = "New"
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_view', args=(ticket_id,)))
