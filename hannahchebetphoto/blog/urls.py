from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('',views.HomeView.as_view(), name='index'),
    path('detail/<int:pk>',views.BlogDetailView.as_view(), name='blog_detail'),
    path('new-post/',views.BlogCreateView.as_view(), name='blog_create'),
    path('delete-post/<int:pk>',views.BlogDeleteView.as_view(), name='blog_delete'),
    path('update-post/<int:pk>',views.BlogUpdateView.as_view(), name='blog_update')

]