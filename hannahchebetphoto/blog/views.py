from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import BlogPost

class HomeView(ListView):
    model = BlogPost
    template_name = 'blog_index.html'

    def get_queryset(self):
        # organize blog posts by created date newest first
        return BlogPost.objects.all().order_by('-created')

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'

class BlogCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_staff'
    model = BlogPost
    template_name = 'blog_create.html'
    fields= ['title','body','images','thumbnail_image']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        # blog author set as the user that creates the blog
        
        form.instance.author = self.request.user
        print(form.is_valid)

        return super().form_valid(form)

class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_staff'
    model = BlogPost
    template_name = 'blog_delete.html'

    success_url = reverse_lazy('blog:index')

class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'is_staff'
    model = BlogPost
    template_name = 'blog_update.html'

    fields= ['title','body','images','thumbnail_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.is_valid)

        return super().form_valid(form)