from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from groups.models import GroupMember
# Create your views here.

class PostList(ListView):
    model = Post    
    
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title','message','group')
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        return super().form_valid(form)
    