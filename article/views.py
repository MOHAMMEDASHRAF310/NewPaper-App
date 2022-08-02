from django.shortcuts import render
from django.views.generic import ListView,DetailView ,CreateView
from django.views.generic.edit import DeleteView,UpdateView
from .models import article
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Create your views here.

class ArticleListView(LoginRequiredMixin,ListView):
    model=article
    template_name = 'article_view.html'
    login_url='login'

class articledetailsview(LoginRequiredMixin,DetailView):
    template_name='Detials.html'
    model= article
    login_url='login'

class articleEdit(LoginRequiredMixin,UpdateView):
    model=article
    template_name='update.html'
    fields=('title','body')
    login_url='login'
    def dispatch(self, request, *args, **kwargs) :
        obj=self.get_object()
        if obj.auther!=self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class articledelete(LoginRequiredMixin,DeleteView):
    model=article
    template_name='Delete.html'
    def dispatch(self, request, *args, **kwargs) : # to prevet any user to edit or delete except the owner of the article
        obj=self.get_object()
        if obj.auther!=self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class createnewarticle(LoginRequiredMixin,CreateView):
    template_name='articlenew.html'
    model=article
    fields=('title','body')
    login_url='login'
    def form_valid(self, form) : # to set the auther who is log in automatically
        form.instance.auther=self.request.user  
        return super().form_valid(form)

