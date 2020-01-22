from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                                DeleteView, UpdateView)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import centers, faculties, fee, quaries, rankers, students
# Create your views here.
class indexview(TemplateView):
    template_name = 'index.html'

class contactview(TemplateView):
    template_name = 'contactus.html'

class ackview(TemplateView):
    template_name = 'ack.html'

##faculties
class facultieslistview(ListView):
    context_object_name = 'faculty'
    model = faculties

class facultiesdetailview(DetailView):
    model = faculties

class facultiescreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/faculties_list.html'
    fields = '__all__'
    model = faculties

class facultiesupdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/faculties_list.html'
    fields = '__all__'
    model = faculties

class facultiesdelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/faculties_list.html'
    model = faculties
    success_url = reverse_lazy("cooperate:faculties_list")

##rankers

class rankerslistview(ListView):
    context_object_name = 'ranker'
    model = rankers

class rankersdetailview(DetailView):
    model = rankers

class rankerscreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/rankers_list.html'
    fields = '__all__'
    model = rankers

class rankersupdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/rankers_list.html'
    fields = '__all__'
    model = rankers

class rankersdelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/rankers_list.html'
    model = rankers
    success_url = reverse_lazy("cooperate:rankers_list")


##centers
class  centerslistview(ListView):
    context_object_name = 'center'
    model = centers

class  centersdetailview(DetailView):
    model = centers

class  centerscreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/centers_list.html'
    fields = '__all__'
    model = centers

class centersupdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/centers_list.html'
    fields = '__all__'
    model = centers

class  centersdelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/centers_list.html'
    model = centers
    success_url = reverse_lazy("cooperate:centers_list")

##students
class  studentslistview(ListView):
    context_object_name = 'student'
    model = students

class  studentsdetailview(DetailView):
    model = students

class  studentscreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/students_list.html'
    fields = '__all__'
    model = students

class studentsupdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/students_list.html'
    fields = '__all__'
    model = students

class  studentsdelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/students_list.html'
    model = students
    success_url = reverse_lazy("cooperate:students_list")

##fees
class  feelistview(ListView):
    context_object_name = 'fees'
    model = fee

class  feedetailview(DetailView):
    model = fee

class  feecreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/fee_list.html'
    fields = '__all__'
    model = fee

class feeupdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/fee_list.html'
    fields = '__all__'
    model = fee

class  feedelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/fee_list.html'
    model = fee
    success_url = reverse_lazy("cooperate:fee_list")

##quaries

class  quarieslistview(ListView):
    context_object_name = 'quary'
    model = quaries

class  quariesdetailview(DetailView):
    model = quaries

class  quariescreate(CreateView):
    fields = '__all__'
    model = quaries

class  quariesdelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'cooperate/quaries_list.html'
    model = quaries
    success_url = reverse_lazy("cooperate:quaries_list")
