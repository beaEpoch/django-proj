from django.urls import path

from .views import index
from .views import PhoneView, CaptchaView, CaptchaDetail, PhoneDetail

urlpatterns = [
    path('dzg/dist/activity.html', index, name='index'),
    path('captcha', CaptchaView.as_view(), name='captcha-view'),
    path('phone', PhoneView.as_view(), name='phone-view'),
    path('captcha/<int:pk>', CaptchaDetail.as_view(), name='captcha-detail'),
    path('phone/<int:pk>', PhoneDetail.as_view(), name='phone-detail'),
]
