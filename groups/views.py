from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from .models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class GroupList(ListView):
    model = Group

class GroupCreate(CreateView,LoginRequiredMixin):
    model = Group
    fields = ('name','description')
    
class GroupDetail(DetailView):
    model = Group
