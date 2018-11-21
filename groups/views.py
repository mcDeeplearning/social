from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,CreateView,
                                DetailView,RedirectView)
from .models import Group, GroupMember
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
class GroupList(ListView):
    model = Group

class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ('name','description')
    
class GroupDetail(DetailView):
    model = Group

class GroupJoin(LoginRequiredMixin,RedirectView):
    
    # 코드 실행 후 리다이렉트 할 주소 설정
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:detail',kwargs={'slug':self.kwargs.get('slug')})
    # 코드실행
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        
        # 이거 실행해
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        # 애러났어?
        except IntegrityError:
            messages.warning(self.request,'already a member')
        # 애러 안남
        else:
            messages.success(self.request,'add a new member')
            
        return super().get(request,*args,**kwargs)
        
class GroupLeave(LoginRequiredMixin,RedirectView):
    # 코드 실행 후 리다이렉트 할 주소 설정
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:detail',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):
        try:
            membership = GroupMember.objects.filter(
                            user = self.request.user,
                            group__slug = self.kwargs.get('slug')
                            ).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request, 'sorry')
        else:
            membership.delete()
            messages.success(self.request, 'delete!!')        
        
        return super().get(request,*args,**kwargs)