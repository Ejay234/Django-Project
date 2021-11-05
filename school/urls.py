from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", views.log_out, name="logout"),
    path("", views.HomeView.as_view(), name="home"),
    path("work/", views.WorkView.as_view(), name="work"),
    path("schedule/", views.ScheduleView.as_view(), name="schedule"),
    path("checklist/", views.CheckListView.as_view(), name="checklist"),
    path("work/new/", views.CreateWorkView.as_view(), name="add_work"),
    path("schedule/new/", views.CreateScheduleView.as_view(), name="add_schedule"),
    path("checklist/new/", views.CreateCheckListView.as_view(), name="add_checklist"),
    path("work/delete/<pk>", views.DeleteWorkView.as_view(), name="delete_work"),
    path("schedule/delete/<pk>", views.DeleteScheduleView.as_view(),
         name="delete_schedule"),
    path("checklist/delete/<pk>", views.DeleteCheckListView.as_view(),
         name="delete_checklist"),
]
