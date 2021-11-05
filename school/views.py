from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Work, Schedule, CheckList
from .forms import WorkForm, ScheduleForm, CheckListForm

# Create your views here.


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "school/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["works"] = Work.objects.all()
        context["schedules"] = Schedule.objects.all()
        context["checklists"] = CheckList.objects.all()
        return context


class WorkView(LoginRequiredMixin, ListView):
    model = Work
    template_name = 'school/work_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["works"] = Work.objects.all()
        return context


class CreateWorkView(LoginRequiredMixin, CreateView):
    model = Work
    template_name = 'school/create_work.html'
    form_class = WorkForm


class DeleteWorkView(LoginRequiredMixin, DeleteView):
    model = Work
    template_name = 'school/delete_work.html'
    success_url = "/work"


class ScheduleView(LoginRequiredMixin, ListView):
    model = Schedule
    template_name = 'school/schedule_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schedules"] = Schedule.objects.all()
        return context


class CreateScheduleView(LoginRequiredMixin, CreateView):
    model = Schedule
    template_name = 'school/create_schedule.html'
    form_class = ScheduleForm


class DeleteScheduleView(LoginRequiredMixin, DeleteView):
    model = Schedule
    template_name = 'school/delete_schedule.html'
    success_url = "/schedule"


class CheckListView(LoginRequiredMixin, ListView):
    model = CheckList
    template_name = 'school/checklist_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["checklists"] = CheckList.objects.all()
        return context


class CreateCheckListView(LoginRequiredMixin, CreateView):
    model = CheckList
    template_name = 'school/create_checklist.html'
    form_class = CheckListForm


class DeleteCheckListView(LoginRequiredMixin, DeleteView):
    model = CheckList
    template_name = 'school/delete_checklist.html'
    success_url = "/checklist"


def log_out(request):
    logout(request)
    return redirect("/")
