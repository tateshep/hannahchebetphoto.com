from django.urls import path
from . import views

app_name = "userprofile"

urlpatterns = [
    path('user-list/',views.UserListView.as_view(), name = "user_list"),
    path('signup/', views.SignUpView.as_view(), name = "signup"),
    path('my-collections/',views.MyCollections.as_view(),name = "my_collections"),
    path('download-image/<int:pk>', views.DownloadPhotoView.as_view(), name = "download"),
]