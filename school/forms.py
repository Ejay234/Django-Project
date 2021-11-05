from django import forms
from django.forms import fields
from .models import Work, Schedule, CheckList


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = "__all__"


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = "__all__"
        widgets = {'day': forms.CheckboxSelectMultiple}


class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = "__all__"
