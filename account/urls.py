from django.urls import path
from .views import userList,profileList,addressList,userDetail,profileDetail,addressDetail

urlpatterns = [
    path('address/<int:pk>/', addressDetail.as_view()),
    path('address/', addressList.as_view()),
    path('profile/<int:pk>/', profileDetail.as_view()),
    path('profile/', profileList.as_view()),
    path('<int:pk>/', userDetail.as_view()),
    path('', userList.as_view()),
]
