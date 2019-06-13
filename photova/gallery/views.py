from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Image, Collection
from .forms import UploadPhotoForm

class HomeView(ListView):
    model = Collection
    template_name = 'gallery.html'
    # not actually sure if this is necessary
    # Update: I think it doesn't because I have it set to all, but if I filtered or ordered, this is where I could do that
    def get_queryset(self):
        return Collection.objects.all()

class CollectionDetail(DetailView):
    model = Collection
    template_name = 'collection_detail.html'

class CollectionCreate(LoginRequiredMixin, CreateView):
    model = Collection
    template_name = 'collection_create.html'
    fields= ['title','description','images']

class CollectionUpdate(LoginRequiredMixin, UpdateView):
    model = Collection
    template_name = 'collection_update.html'
    fields= ['title','description','images']

class CollectionDelete(LoginRequiredMixin, DeleteView):
    model = Collection
    template_name = 'collection_delete.html'
    success_url = reverse_lazy('gallery:gallery')

class NewImage(LoginRequiredMixin, CreateView):
    model = Image
    # form_class = UploadPhotoForm
    template_name = 'image_new.html'
    fields = ['title','photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('gallery:gallery')

class ImageDetail(DetailView):
    model = Image
    template_name = 'image_detail.html'

class ImageUpdate(LoginRequiredMixin, UpdateView):
    model = Image
    template_name = 'image_update.html'
    fields = ['title','author','photo']

class ImageDelete(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image_delete.html'
    success_url = reverse_lazy('gallery:gallery')