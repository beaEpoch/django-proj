from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Phone, Captcha
from .serializer import PhoneSerializer, CaptchaSerializer


def index(request):
    act_type = request.GET.get('act_type')
    if act_type == '1':
        return render(request, '15.html')
    elif act_type == '2':
        return render(request, '30.html')
    elif act_type == '3':
        return render(request, '45.html')
    else:
        return render(request, '60.html')


class PhoneView(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    # permission_classes = (IsAuthenticated)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('status', 'kind')


class CaptchaView(generics.ListCreateAPIView):
    queryset = Captcha.objects.all()
    serializer_class = CaptchaSerializer
    # permission_classes = (IsAuthenticated)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('phone',)


class PhoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    # permission_classes = (IsAuthenticated)


class CaptchaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Captcha.objects.all()
    serializer_class = CaptchaSerializer
    # permission_classes = (IsAuthenticated)
