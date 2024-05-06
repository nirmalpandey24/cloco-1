from django.urls import path
from .views import CustomUserDetail, CustomUserInfo

urlpatterns = [
    path("customuser/", CustomUserDetail.as_view(), name="customuser-detail"),
    path("customuser/<int:id>/", CustomUserInfo.as_view(), name="customuser-info"),
]
