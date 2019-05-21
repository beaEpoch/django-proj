from django.urls import path

from .views import index15
from .views import PhoneView, CaptchaView, PhoneDetail

urlpatterns = [
    path('15', index15, name='index15'),
    # path('15', views.index15, name='index15'),
    path('captcha', CaptchaView.as_view(), name='captcha-view'),
    path('phone', PhoneView.as_view(), name='phone-view'),
    path('phone/<int:pk>', PhoneDetail.as_view(), name='phone-detail'),
]