from django.db import models
from django.urls import reverse
from datetime import timedelta

from gallery.models import Image

class BlogPost(models.Model):
    # Blog model. Has a manytomany relationship with Image from gallery
    # allowing a group of images to be included in the blog. 
    # the foreign key relationship with Image sets the thumbnail image which is 
    # displayed on the blog card in the index view and in the post itself.
    # thumbnail_image requires the related name so as not to be confused by django 
    # with the other images relationship

    title = models.CharField(max_length=40)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(Image,blank=True)
    thumbnail_image= models.ForeignKey(Image,related_name="thumbnails", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse('blog:blog_detail', args=(self.pk,))

