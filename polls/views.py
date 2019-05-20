from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PhoneCaptcha


def index15(request):
    return render(request, '15.html')


def getPhone(request):
    return HttpResponse('123')


def getCaptcha(request):
    return HttpResponse('456')

class PhoneView(generics.ListCreateAPIView):
    queryset = PhoneCaptcha.objects.all()
    serializer_class = PhoneCaptchaSerializer
    permission_classes = (IsAuthenticated)

    def get_queryset(self):
        queryset = PhoneCaptcha.objects.filter(
            creator=self.request.user
        ).all()
        return queryset
