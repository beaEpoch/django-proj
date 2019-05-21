from rest_framework import serializers
from .models import Phone, Captcha

class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = ('id', 'phone', 'kind', 'status', 'created')


class CaptchaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Captcha
        fields = ('id', 'phone', 'captcha', 'created')