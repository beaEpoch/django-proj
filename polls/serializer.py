from rest_framework import serializers
from .models import PhoneCaptcha

class PhoneCaptchaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneCaptcha
        fields = ('id', 'phone', 'captcha', 'kind', 'created')