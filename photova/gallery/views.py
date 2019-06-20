from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.admin.views.decorators import user_passes_test

from .models import Image, Collection
from .forms import UploadPhotoForm

class HomeView(ListView):
    model = Collection
    template_name = 'gallery.html'

    def get_queryset(self):
        return Collection.objects.all().filter(showcase_gallery=True)

class CollectionDetail(DetailView):
    model = Collection
    template_name = 'collection_detail.html'


class CollectionCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'is_staff'
    model = Collection
    template_name = 'collection_create.html'
    fields= ['title','description','images','showcase_gallery']


class CollectionUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'is_staff'
    model = Collection
    template_name = 'collection_update.html'
    fields= ['title','description','images','showcase_gallery']


class CollectionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_staff'
    model = Collection
    template_name = 'collection_delete.html'
    success_url = reverse_lazy('gallery:gallery')

class NewImage(PermissionRequiredMixin, CreateView):
    permission_required = 'is_staff'
    model = Image
    form_class = UploadPhotoForm
    template_name = 'image_new.html'
    success_url = reverse_lazy('gallery:gallery')
    # fields = ['title','photo']

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self,request, *args,**kwargs):
        i = 0
        form_class= self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('photo')
        if form.is_valid():
            for f in files:
                print(form)
                image = Image()
                if i == 0:
                    image.title = form.instance.title
                else:
                    image.title = form.instance.title + str(i)

                image.author = self.request.user
                image.photo = f
                i += 1
                image.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)


class ImageDetail(DetailView):
    model = Image
    template_name = 'image_detail.html'


class ImageUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'is_staff'
    model = Image
    template_name = 'image_update.html'
    fields = ['title','author','photo']


class ImageDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_staff'
    model = Image
    template_name = 'image_delete.html'
    success_url = reverse_lazy('gallery:gallery')