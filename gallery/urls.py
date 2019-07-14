from django.urls import path

from . import views

app_name = "gallery"

urlpatterns = [
    path('',views.HomeView.as_view(), name='gallery'),
    path('new-image/',views.NewImage.as_view(), name='new'),
    path('image-detail/<int:pk>',views.ImageDetail.as_view(), name='image_detail'),
    path('image-delete/<int:pk>',views.ImageDelete.as_view(), name='delete_image'),
    path('image-update/<int:pk>',views.ImageUpdate.as_view(), name='image_update'),
    path('collection-create/',views.CollectionCreate.as_view(), name='collection_create'),
    path('collection-detail/<int:pk>',views.CollectionDetail.as_view(), name='collection_detail'),
    path('collection-update/<int:pk>',views.CollectionUpdate.as_view(), name='collection_update'),
    path('collection-delete/<int:pk>',views.CollectionDelete.as_view(), name='collection_delete'),
]

