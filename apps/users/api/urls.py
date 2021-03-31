from django.urls import path
from apps.users.api.api import UserAPIView, UserDetailAPIView

urlpatterns = [
    path('', UserAPIView.as_view(), name="user_api"),
    path('<int:pk>', UserDetailAPIView.as_view(), name="user_detail_api"),
]
