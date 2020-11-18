from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("view/<id>", views.view_employee, name="view-employee"),
    path("add/", views.add_employee, name="add-employee"),
    path("edit/<id>", views.edit_employee, name="edit-employee"),
    path("delete/<id>", views.delete_employee, name="delete-employee"),
]
