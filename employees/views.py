from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm


def dashboard(request):

    context = {}

    employees = Employee.objects.all()

    context["employees"] = employees
    context["title"] = "Dashboard"

    return render(request, "employees/dashboard.html", context)


def view_employee(request, id):
    context = {}

    obj = get_object_or_404(Employee, id=id)

    context["employee"] = obj
    context["title"] = "View"

    return render(request, "employees/view_employee.html", context)


def add_employee(request):
    context = {}

    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Emloyee Added Successfuly")
        return redirect("dashboard")

    context["form"] = form
    context["title"] = "Add-Employee"

    return render(request, "employees/add_employee.html", context)


def edit_employee(request, id):

    context = {}

    obj = get_object_or_404(Employee, id=id)

    form = EmployeeForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, "Edit Successfuly")
        return redirect("dashboard")

    context["form"] = form
    context["title"] = "Edit Employee"

    return render(request, "employees/edit_employee.html", context)


def delete_employee(request, id):
    delete_employee = Employee.objects.get(id=id)
    delete_employee.delete()

    messages.success(request, "Deleted Successful")

    return redirect("dashboard")
