from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('creat_targets/', views.creat_target, name="creat_tar"),
    path('show_targets/', views.showtarget, name="show_tar"),
    path('ToDo_edit/<int:id>', views.edit_ToDo, name="edit_tar"),
    path('ToDo_delete/<int:id>', views.Delete, name="delete_tar"),
]
