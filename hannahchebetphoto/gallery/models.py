from django.db import models
from django.urls import reverse


class Image(models.Model):
    # Image model. Uses ImageField to allow user to upload image.

    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='data/')

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse('gallery:image_detail', args=(self.pk,))


class Collection(models.Model):
    # Collection, has a many to many relationship with the Image model
    # as well as with permitted users. Permitted users will be able to view 
    # collections associated with them in the My Collections view

    title = models.CharField(max_length=50)
    images = models.ManyToManyField(Image,blank=True) # manytomany relationship with Collection
    description = models.TextField(blank=True)
    showcase_gallery = models.BooleanField(default=False)
    permitted_users = models.ManyToManyField('auth.User',blank=True)
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse('gallery:collection_detail', args=[str(self.id)])

